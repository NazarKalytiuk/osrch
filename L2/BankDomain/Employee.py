class Employee(object):
    EmployeeCode = property()

    @EmployeeCode.getter
    def EmployeeCode(self):
        return self.EmployeeCode

    @EmployeeCode.setter
    def EmployeeCode(self, value):
        self.EmployeeCode = value

    Pib = property()

    @Pib.getter
    def Pib(self):
        return self.Pib

    @Pib.setter
    def Pib(self, value):
        self.Pib = value

    Age = property()
    @Age.getter
    def Age(self):
        return  self.Age

    @Age.setter
    def Age(self, value):
        self.Age = value

    Address = property()

    @Address.getter
    def Address(self):
        return self.Address

    @Address.setter
    def Address(self, value):
        self.Address = value

    PassportData = property()

    @PassportData.getter
    def PassportData(self):
        return self.PassportData

    @PassportData.setter
    def PassportData(self, value):
        self.PassportData = value

    RoleCode = property()

    @RoleCode.getter
    def RoleCode(self):
        return self.RoleCode

    @RoleCode.setter
    def RoleCode(self, value):
        self.RoleCode = value

