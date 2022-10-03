import json

from core.settings import FILE_PROFILE

from core.utils.text import color
from core.utils.file import write_file
from core.base.error import print_error_estrange


class JsonDataProfile():
    
    def __init__(self, json_data: dict, module: str) -> None:
        self.file_profile = FILE_PROFILE
        self.json_data = json_data
        self.module = module

    def json_search_key(self, module: str, key: str, value: str):
        for item in self.json_data[module]:
            for i,x in enumerate(self.json_data[module][item]):
                try:
                    if x[key] == value:
                        return self.json_data[module][item].pop(i)

                except Exception as error:
                    print_error_estrange(error)

    def json_save(self, category: str, new_dict: dict):
        if self.json_data[self.module].get(category):
            self.json_data[self.module][category].append(new_dict)
        else:
            self.json_data[self.module][category] = [new_dict]

        write_file(
            content=json.dumps(self.json_data, indent=4),
            path_file=self.file_profile
        )

        _id = new_dict.get("id")
        message = f"Command: {self.command} - ID: {_id}"

        self.log.info(message)

        print(
            color(
                text=message,
                types=['bold', 'green']
            )
        )
