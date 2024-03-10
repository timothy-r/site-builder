from site_gen.reader.reader import Reader
from site_gen.reader.html_reader import HTMLReader
from site_gen.reader.yaml_reader import YAMLReader

class ReaderFactory:

    def get_reader(self, file:str) -> Reader:
        """
            return a reader for this type of file
        """
        pass