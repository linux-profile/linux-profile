from linux_profile.utils.text import (
    Colors,
    color,
    slugify,
    asterisk
)


def test_utils_slugify_hairline():
    text = slugify(value="linux profile", slug_type="-")
    assert text == 'linux-profile'


def test_utils_slugify_underline():
    text = slugify(value="linux profile", slug_type="_")
    assert text == 'linux_profile'


def test_utils_slugify_lower():
    text = slugify(value="LINUXPROFILE", slug_type="_")
    assert text == 'linuxprofile'


def test_utils_color_violett():
    text = color(text=" linux ", types=['violett'])
    assert text[0:5] == Colors.VIOLETT


def test_utils_color_blue():
    text = color(text=" linux ", types=['blue'])
    assert text[0:5] == Colors.BLUE


def test_utils_color_cyan():
    text = color(text=" linux ", types=['cyan'])
    assert text[0:5] == Colors.CYAN


def test_utils_color_green():
    text = color(text=" linux ", types=['green'])
    assert text[0:5] == Colors.GREEN


def test_utils_color_yellow():
    text = color(text=" linux ", types=['yellow'])
    assert text[0:5] == Colors.YELLOW


def test_utils_color_red():
    text = color(text=" linux ", types=['red'])
    assert text[0:5] == Colors.RED


def test_utils_color_endc():
    text = color(text=" linux ", types=['yellow'])
    total = len(text)
    assert text[total-4:total] == Colors.ENDC


def test_utils_color_bold():
    text = color(text=" linux ", types=['bold'])
    assert text[0:4] == Colors.BOLD


def test_utils_color_underline():
    text = color(text=" linux ", types=['underline'])
    assert text[0:4] == Colors.UNDERLINE


def test_utils_color_dark_gray():
    text = color(text=" linux ", types=['dark_gray'])
    assert text[0:10] == Colors.DARK_GRAY


def test_utils_asterisk():
    assert asterisk() == '\x1b[1m\x1b[91m* \x1b[0m'
