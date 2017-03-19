class Role(object):
    RoleCode = property()
    @RoleCode.getter
    def RoleCode(self):
        return self.RoleCode

    @RoleCode.setter
    def RoleCode(self, value):
        self.RoleCode = value

    Title = property()

    @Title.getter
    def Title(self):
        return self.Title
    @Title.setter
    def Title(self, value):
        self.Title = value

    Salary = property()
    @Salary.getter
    def Salary(self):
        return self.Salary
    @Salary.setter
    def Salary(self, value):
        self.Salary = value
    Duties = property()
    @Duties.getter
    def Duties(self):
        return self.Duties
    @Duties.setter
    def Duties(self, value):
        self.Duties = value

    Requirements=property()
    @Requirements.getter
    def Requirenments(self):
        return self.Requirements
    @Requirements.setter
    def Requirenments(self, value):
        self.Requirements = value