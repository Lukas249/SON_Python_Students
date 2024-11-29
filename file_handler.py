from abc import abstractmethod

class BaseFileSaver:

    @staticmethod
    @abstractmethod
    def save(path: str, lines: list[str]):
        pass


class BaseFileLoader:

    @staticmethod
    @abstractmethod
    def load(path: str):
        pass

class FileHandler(BaseFileSaver, BaseFileLoader):

    @staticmethod
    def load(path: str):
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        return lines

    @staticmethod
    def save(path: str, lines: list[str]):
        file = open(path, "w")
        file.writelines(lines)
        file.close()