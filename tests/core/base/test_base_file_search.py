from linux_profile.base.file import BaseSearch


file_path = "./tests/helpers/database.json"


def test_base_search_module():
    data = BaseSearch(file_path)
    index = data._module("script")

    assert len(index) == 1
    assert index == ['script']
    assert type(data.json[index[0]]) == dict


def test_base_search_tag():
    data = BaseSearch(file_path)
    index = data._tag(key="init")

    assert len(index) == 2
    assert index == ['script', 'init']
    assert type(data.json[index[0]][index[1]]) == list


def test_base_search_item():
    id = "A48D2542AF3045888DC1242EF77C7666"
    data = BaseSearch(file_path)
    index = data._item(key="id", value=id)

    assert len(index) == 4
    assert index == ['package', 'python', 0, 'id']
    assert data.json[index[0]][index[1]][index[2]][index[3]] == id
