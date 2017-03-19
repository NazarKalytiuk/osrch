class Role(object):
    __RoleCode = 0
    @property
    def RoleCode(self):
        return self.__RoleCode

    @RoleCode.setter
    def RoleCode(self, value):
        self.__RoleCode = value

    __Title = ''

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, value):
        self.__Title = value

    __Salary = 0
    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, value):
        self.__Salary = value
    __Duties = ''
    @property
    def Duties(self):
        return self.__Duties
    @Duties.setter
    def Duties(self, value):
        self.__Duties = value

    __Requirements = ''
    @property
    def Requirements(self):
        return self.__Requirements

    @Requirements.setter
    def Requirements(self, value):
        self.__Requirements = value