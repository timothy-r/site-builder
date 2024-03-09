from site_gen.reader.reader import Reader


class ReaderFactory:

    def get_reader(self, file:str) -> Reader:
        """
            return a reader for this type of file
        """
        pass