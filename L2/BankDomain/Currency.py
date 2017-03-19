class Currency(object):
    __CurrencyCode = 0

    @property
    def CurrencyCode(self):
        return self.__CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, value):
        self.__CurrencyCode = value

    __Title = ''

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, value):
        self.__Title = value

    __Course = 0.00

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        self.__Course = value