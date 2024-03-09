import os
import yaml

class YAMLFile():

    def __init__(self, path:str) -> None:
        self._path = path

    def read(self) -> dict:
        if os.path.exists(path=self._path):
            with open(self._path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return data
        else:
            return {}

    def write(self, data:dict) -> None:
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(yaml.safe_dump(data=data))