from os import path, remove
from linux_profile.base.file import BaseFile
from linux_profile.base.error import ErrorFile


file_path = "./tests/helpers"


def test_base_file_read_success():
    text = BaseFile()
    result = text.read(path_file=f"{file_path}/read.txt")
    assert result == 'Unit Test LinuxProfile'


def test_base_file_write_success():
    test_path = f"{file_path}/write.txt"

    text = BaseFile()
    text.write(content="xpto", path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)


def test_base_file_read_lines_success():
    text = BaseFile()
    result = text.read_lines(path_file=f"{file_path}/read_lines.txt")
    assert len(result) == 10


def test_base_file_write_lines_success():
    test_path = f"{file_path}/write_lines.txt"

    text = BaseFile()
    text.write_lines(content=["xpto"], path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)


def test_base_file_read_error():
    text = BaseFile()
    try:
        text.read(path_file=f"{file_path}/xpto.txt")
    except Exception as error:
        assert error.__class__ == ErrorFile


def test_base_file_read_lines_error():
    text = BaseFile()
    try:
        text.read_lines(path_file=f"{file_path}/xpto.txt")
    except Exception as error:
        assert error.__class__ == ErrorFile


def test_base_file_touch_success():
    test_path = f"{file_path}/touch.json"

    text = BaseFile()
    text.touch(test_path)
    assert path.exists(test_path) == True
    remove(test_path)
