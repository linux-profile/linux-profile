from json import loads
from linux_profile.base.file import File
from linux_profile.base.action import Action


file_path = "./tests/helpers/database.json"


def test_base_action_create():
    action = Action(file_path)

    content_create = {"id": 1, "name": "Linux"}

    action._create_item(content=content_create, module="script", tag="init")
    content = loads(File.read(path_file=file_path))

    assert content["script"]["init"][1] == content_create
    action._delete_item(value=1)


def test_base_action_update():
    id = "EE959D7607694622B030BEEA1174AF56"
    action = Action(file_path)

    content = loads(File.read(path_file=file_path))
    assert content["script"]["init"][0]["name"] == "echo"

    action._update_item(content={"name": "linux"}, value=id)
    content = loads(File.read(path_file=file_path))
    assert content["script"]["init"][0]["name"] == "linux"

    action._update_item(content={"name": "echo"}, value=id)
    content = loads(File.read(path_file=file_path))
    assert content["script"]["init"][0]["name"] == "echo"


def test_base_action_delete():
    action = Action(file_path)

    initial_content = loads(File.read(path_file=file_path))
    assert len(initial_content["package"]["python"]) == 1

    action._delete_item(value="A48D2542AF3045888DC1242EF77C7666")
    final_ontent = loads(File.read(path_file=file_path))
    assert len(final_ontent["package"]["python"]) == 0

    action._create_item(
        content=initial_content["package"]["python"][0],
        module="package",
        tag="python"
    )
