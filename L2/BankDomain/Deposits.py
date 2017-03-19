class Deposit(object):
    __DepositeCode = 0

    @property
    def DepositeCode(self):
        return self.__DepositeCode

    @DepositeCode.setter
    def DepositeCode(self, value):
        self.__DepositeCode = value

    __Title = ''

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, value):
        self.__Title = value

    __MinTherm = 0

    @property
    def MinTherm(self):
        return self.__MinTherm

    @MinTherm.setter
    def MinTherm(self, value):
        self.__MinTherm = value

    __MinSum = 0

    @property
    def MinSum(self):
        return self.__MinSum

    @MinSum.setter
    def MinSum(self, value):
        self.__MinSum = value

    __CurrencyCode = 0

    @property
    def CurrencyCode(self):
        return self.__CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, value):
        self.__CurrencyCode = value

    __AdditionalCondition = ''

    @property
    def AdditionalCondition(self):
        return self.__AdditionalCondition

    @AdditionalCondition.setter
    def AdditionalCondition(self, value):
        self.__AdditionalCondition = value