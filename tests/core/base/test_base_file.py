from os import path, remove
from linux_profile.base.file import File
from linux_profile.base.error import ErrorFile


file_path = "./tests/helpers"


def test_base_file_read_success():
    text = File()
    result = text.read(path_file=f"{file_path}/read.txt")
    assert result == 'Unit Test LinuxProfile'


def test_base_file_write_success():
    test_path = f"{file_path}/write.txt"

    text = File()
    text.write(content="xpto", path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)


def test_base_file_read_lines_success():
    text = File()
    result = text.read_lines(path_file=f"{file_path}/read_lines.txt")
    assert len(result) == 10


def test_base_file_write_lines_success():
    test_path = f"{file_path}/write_lines.txt"

    text = File()
    text.write_lines(content=["xpto"], path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)


def test_base_file_read_file_does_not_exist_error():
    test_path = f"{file_path}/xpto.txt"
    text = File()

    text.read(path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)

def test_base_file_read_lines_file_does_not_exist_error():
    test_path = f"{file_path}/xpto.txt"
    text = File()

    text.read_lines(path_file=test_path)
    assert path.exists(test_path) == True
    remove(test_path)

def test_base_file_touch_success():
    test_path = f"{file_path}/touch.json"

    text = File()
    text.touch(test_path)
    assert path.exists(test_path) == True
    remove(test_path)
