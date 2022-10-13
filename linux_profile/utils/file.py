from os import system
from linux_profile.settings import FILE


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
                info_value = item[index+1:len(item)] \
                    .replace('"', '').replace('|', ' ')

                if info_value[0] == ' ':
                    info_value = info_value[1:len(info_value)]

                my_info.update({info_name: info_value})

    return my_info


def write_file(
        content: str,
        path_file: str,
        type_file: str = '',
        mode: str = 'w') -> str:
    with open(path_file + type_file, mode) as outfile:
        outfile.write(content)


def read_file(path_file: str, type_file: str = '') -> str:
    with open(path_file + type_file, 'r', encoding='utf8') as content:
        content = content.read()
    return content


def get_system() -> dict:
    """Get System Information

    Returns
    -------
    dict
        Dictionary with contents of the .hostnamectl file.
    """
    path_system = FILE.get("system")

    system('hostnamectl > ' + path_system)
    file_system = read_file(path_file=path_system)

    system('rm ' + path_system)
    content = get_content(path_file=file_system, separator=":")

    return {
        "kernel": content.get('kernel'),
        "static_host_name": content.get('statichostname'),
        "hardware_vendor": content.get('hardwarevendor'),
        "hardware_model": content.get('hardwaremodel'),
        "architecture": content.get('architecture'),
        "icon_name": content.get('iconname'),
        "chassis": content.get('chassis')
    }


def get_distro() -> dict:
    """Get Linux distribution

    Returns
    -------
    dict
        Dictionary with contents of the .os-release file.
    """
    path_distro = FILE.get("distro")
    system("cat /etc/os-release > " + path_distro)

    file_distro = read_file(path_file=path_distro)
    system('rm ' + path_distro)

    content = get_content(path_file=file_distro, separator="=")
    return {
        "name": content.get('name'),
        "pretty_name": content.get('pretty_name'),
        "version_id": content.get('version_id'),
        "version": content.get('version'),
    }
