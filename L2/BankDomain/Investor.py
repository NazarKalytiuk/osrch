class Investor(object):
    __investorCode=0

    @property
    def InvestorCode(self):
        return self.__investorCode

    @InvestorCode.setter
    def InvestorCode(self, value):
        self.__investorCode = value

    __DepositeCode = 0

    @property
    def DepositeCode(self):
        return self.__DepositeCode
    @DepositeCode.setter
    def DepositeCode(self, value):
        self.__DepositeCode = value

    __Pib = ''

    @property
    def Pib(self):
        return self.__Pib

    @Pib.setter
    def Pib(self, value):
        self.__Pib = value

    __DepositeSum = 0

    @property
    def DepositeSum(self):
        return self.__DepositeSum

    @DepositeSum.setter
    def DepositeSum(self, value):
        self.__DepositeSum = value

    __DepositeEnded = 0

    @property
    def DepositeEnded(self):
        return self.__DepositeEnded

    @DepositeEnded.setter
    def DepositeEnded(self, value):
        self.__DepositeEnded = value

    _EmployeeCode = 0

    @property
    def EmployeeCode(self):
        return self.__EmployeeCode

    @EmployeeCode.setter
    def EmployeeCode(self, value):
        self.__EmployeeCode = value

    __Address = ''

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, value):
        self.__Address = value

    __Phone = ''

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, value):
        self.__Phone = value

    __PassportData = property()

    @property
    def PassportData(self):
        return self.__PassportData

    @PassportData.setter
    def PassportData(self, value):
        self.__PassportData = value

    __DepositeDate = ''

    @property
    def DepositeDate(self):
        return self.__DepositeDate

    @DepositeDate.setter
    def DepositeDate(self, value):
        self.__DepositeDate = value

    __EndDepositeDate = ''

    @property
    def EndDepositeDate(self):
        return self.__EndDepositeDate

    @EndDepositeDate.setter
    def EndDepositeDate(self, value):
        self.__EndDepositeDate = value
