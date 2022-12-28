from os import path, remove
from linux_profile.utils.file import read_file, read_lines_file, write_file


file_path = "./tests/utils/file"


def test_utils_read_file_success():
    test_path = f"{file_path}/read_file.txt"
    text = read_file(path_file=test_path)

    assert text == 'Unit Test LinuxProfile'


def test_utils_read_lines_file_success():
    test_path = f"{file_path}/read_lines_file.txt"
    text = read_lines_file(path_file=test_path)

    assert len(text) == 10
    assert text[0] == '0\n'


def test_utils_file_write_without_extension_success():
    test_path = f"{file_path}/write_file"
    text = "Unit Test LinuxProfile"

    write_file(content=text, path_file=test_path)
    assert path.isfile(test_path) == True
    remove(test_path)


def test_utils_file_write_with_extension_success():
    test_path = f"{file_path}/write_file"
    text = "Unit Test LinuxProfile"

    write_file(content=text, path_file=test_path, type_file=".txt")
    assert path.isfile(f"{test_path}.txt") == True
    remove(f"{test_path}.txt")
