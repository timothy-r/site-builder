import os
from bs4 import BeautifulSoup as bs

class HTMLFile():

    def __init__(self, path:str) -> None:
        self._path = path

    def read(self) -> bs:
        if os.path.exists(path=self._path):
            with open(self._path, 'r', encoding='utf-8') as file:
                return bs(markup=file.read(), features='html.parser')

        return None

    def write(self, dom_doc:bs) -> None:
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(dom_doc.prettify())