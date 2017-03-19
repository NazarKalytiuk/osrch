class Employee(object):
    __EmployeeCode = 0

    @property
    def EmployeeCode(self):
        return self.__EmployeeCode

    @EmployeeCode.setter
    def EmployeeCode(self, value):
        self.__EmployeeCode = value

    __Pib = ''

    @property
    def Pib(self):
        return self.__Pib

    @Pib.setter
    def Pib(self, value):
        self.__Pib = value

    __Age = 0
    @property
    def Age(self):
        return  self.__Age

    @Age.setter
    def Age(self, value):
        self.__Age = value

    __Address = ''

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, value):
        self.__Address = value

    __PassportData = property()

    @property
    def PassportData(self):
        return self.__PassportData

    @PassportData.setter
    def PassportData(self, value):
        self.__PassportData = value

    __RoleCode = 0

    @property
    def RoleCode(self):
        return self.__RoleCode

    @RoleCode.setter
    def RoleCode(self, value):
        self.__RoleCode = value

