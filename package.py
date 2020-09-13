class Package:

    def __init__(self, name, version=''):
        self.__name = name
        self.__version = version
        self.__dependencies = None

    def get_name(self):
        return self.__name

    def get_version(self):
        return self.__version

    def get_dependencies(self):
        return self.__dependencies

    def set_dependencies(self, dependencies):
        self.__dependencies = dependencies
