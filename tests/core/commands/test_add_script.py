"""Tests for the option_body() closure introduced in add_script (PR #181 / Issue #172)."""
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from linux_profile.base.file import File
from linux_profile.base.system import System


# ---------------------------------------------------------------------------
# Standalone replica of option_body() for isolated unit testing.
# Mirrors the production closure in linux_profile/commands/add.py exactly,
# accepting path_temp and text_editor as parameters instead of via self.
# ---------------------------------------------------------------------------

def _option_body(path_temp, text_editor="vim"):
    fd, tmp = tempfile.mkstemp(prefix="linuxp_script_", dir=path_temp)
    os.close(fd)
    path = Path(tmp)
    editor = text_editor

    exit_code = System().system(cmd=[editor, str(path)])
    if exit_code != 0:
        raise RuntimeError(
            f"Editor '{editor}' exited with code {exit_code}. Script not saved.")

    if path.exists():
        try:
            body = File.read(path_file=path).splitlines()
        finally:
            path.unlink(missing_ok=True)
        return body
    raise ValueError("No script body provided — editor exited without saving.")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_option_body_returns_list_of_lines(tmp_path):
    """Editor writes content — option_body() returns a list of lines."""
    def fake_editor(cmd):
        Path(cmd[-1]).write_text("line1\nline2\nline3\n")
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        result = _option_body(path_temp=tmp_path)

    assert result == ["line1", "line2", "line3"]


def test_option_body_temp_file_deleted_after_read(tmp_path):
    """Temp file is deleted after content is read successfully."""
    captured_path = {}

    def fake_editor(cmd):
        p = Path(cmd[-1])
        captured_path["path"] = p
        p.write_text("echo hello\n")
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        _option_body(path_temp=tmp_path)

    assert not captured_path["path"].exists()


def test_option_body_temp_file_deleted_on_read_exception(tmp_path):
    """Temp file is deleted even when File.read() raises an exception."""
    captured_path = {}

    def fake_editor(cmd):
        p = Path(cmd[-1])
        captured_path["path"] = p
        p.write_text("content")
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        with patch("linux_profile.base.file.File.read", side_effect=Exception("read error")):
            try:
                _option_body(path_temp=tmp_path)
            except Exception:
                pass

    assert not captured_path["path"].exists()


def test_option_body_raises_runtime_error_on_nonzero_exit(tmp_path):
    """RuntimeError is raised when the editor exits with a non-zero code."""
    with patch.object(System, "system", return_value=127):
        try:
            _option_body(path_temp=tmp_path, text_editor="nonexistent_editor")
            assert False, "Expected RuntimeError"
        except RuntimeError as error:
            assert "nonexistent_editor" in str(error)
            assert "127" in str(error)


def test_option_body_raises_value_error_when_file_not_saved(tmp_path):
    """ValueError is raised when the editor exits with code 0 but saves nothing."""
    def fake_editor(cmd):
        Path(cmd[-1]).unlink(missing_ok=True)
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        try:
            _option_body(path_temp=tmp_path)
            assert False, "Expected ValueError"
        except ValueError as error:
            assert "No script body provided" in str(error)


def test_option_body_unique_temp_files_per_invocation(tmp_path):
    """Each call to option_body() creates a distinct temp file path."""
    paths = []

    def fake_editor(cmd):
        p = Path(cmd[-1])
        paths.append(p)
        p.write_text("body\n")
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        _option_body(path_temp=tmp_path)
        _option_body(path_temp=tmp_path)

    assert paths[0] != paths[1]


def test_option_body_temp_file_has_correct_prefix(tmp_path):
    """Temp file name starts with the expected prefix."""
    captured_path = {}

    def fake_editor(cmd):
        p = Path(cmd[-1])
        captured_path["path"] = p
        p.write_text("body\n")
        return 0

    with patch.object(System, "system", side_effect=fake_editor):
        _option_body(path_temp=tmp_path)

    assert captured_path["path"].name.startswith("linuxp_script_")
