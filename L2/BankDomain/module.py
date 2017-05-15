class module(object):
    __Id = 0

    @property
    def Id(self):
        return self.__Id

    @Id.setter
    def Id(self, value):
        self.__Id = value

    __Title = ''

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, value):
        self.__Title = value
