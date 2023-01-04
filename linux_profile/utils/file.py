def write_file(
        content: str,
        path_file: str,
        type_file: str = '',
        mode: str = 'w') -> str:
    with open(path_file + type_file, mode) as outfile:
        outfile.write(content)


def read_file(
        path_file: str,
        type_file: str = '') -> str:
    with open(path_file + type_file, 'r', encoding='utf8') as content:
        return content.read()


def read_lines_file(
        path_file: str,
        type_file: str = '') -> list:
    with open(path_file + type_file, 'r', encoding='utf8') as content:
        return content.readlines()


def write_lines_file(
        content: list,
        path_file: str,
        type_file: str = '',
        mode: str = 'w') -> list:
    with open(path_file + type_file, mode) as outfile:
        outfile.writelines(content)


# TODO: This method will be removed in the future.
def get_content(path_file: str, separator: str):
    """Get the contents of a file.

    Parameters
    ----------
    path_file : str
        Name of the file to be formatted.
    separator: str
        Content separator type. Example "=" or ":".

    Returns
    -------
    dict
        Dictionary with file contents.
    """
    my_info = dict()

    file_list = path_file.replace(' ', '|').replace('\n', ' ').split()
    for item in file_list:
        info_name = None
        info_value = None

        for index, value in enumerate(item):
            if value == separator:
                info_name = item[0:index].lower().replace('|', '')
                info_value = item[index + 1:len(item)] \
                    .replace('"', '').replace('|', ' ')

                if info_value[0] == ' ':
                    info_value = info_value[1:len(info_value)]

                my_info.update({info_name: info_value})

    return my_info
