from functools import reduce


class Colors:
    VIOLETT = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DARK_GRAY = '\033[1;30;40m'


def color(text: str, types: list):
    types_sancii = ''
    for item in types:
        types_sancii = types_sancii + getattr(Colors, item.upper())

    return reduce(lambda x, y: x + y, types_sancii) + text + Colors.ENDC


def cleaning_option(text: str):
    list_str = [" ", "\t", "\n", "\"", "\'", "'", "\u001b[C", "\u001b[D"]

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


def print_item(module: str, tag: str, item: str) -> None:
    print(
        color(text=f" {module} ", types=['bold', 'dark_gray']),
        color(text="- Tag:", types=['bold']), tag, "-", item
    )