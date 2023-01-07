import re
from functools import reduce


class Colors:

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    ENDC = "\033[0m"
    VIOLETT = '\033[95m'


def color(text: str, types: list):
    types_sancii = ''
    for item in types:
        types_sancii = types_sancii + getattr(Colors, item.upper())

    return reduce(lambda x, y: x + y, types_sancii) + text + Colors.ENDC


def slugify(value: str, slug_type: str = '_'):
    value = value.lower().strip()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[\s_-]+', slug_type, value)
    value = re.sub(r'^-+|-+$', '', value)
    return value


def cleaning_option(text: str):
    list_str = ["\t", "\n", "\"", "\'", "'", "\u001b[C", "\u001b[D", "\\"]
    for item in list_str:
        text = text.replace(item, "")
    return text


def asterisk():
    return color("* ", types=['bold', 'red'])


def option(
        text: str,
        required: bool = False,
        body: bool = False,
        output: list = None,
        output_list: list = list()):
    option = asterisk() + text if required else text

    if body:
        print(option, "To finish type", color("[end]", ['bold', 'green']))
        while output != 'end':
            output = input("> ")
            if output != 'end':
                output_list.append(output)
        return output_list

    else:
        return input(option)


def print_item(module: str, tag: str, item: str, description: str, id='') -> None:
    description = description if description else 'No description'

    print(
        color(text=id, types=['bold', 'green']),
        color(text=f"Tag: {tag}".ljust(20), types=['bold']),
        item.ljust(25),
        description
    )
