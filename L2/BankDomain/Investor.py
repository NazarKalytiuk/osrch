class Investor(object):
    InvestorCode = property()

    @InvestorCode.getter
    def InvestorCode(self):
        return self.InvestorCode

    @InvestorCode.setter
    def InvestorCode(self, value):
        self.InvestorCode = value


    DepositeCode = property()

    @DepositeCode.getter
    def DepositeCode(self):
        return self.DepositeCode
    @DepositeCode.setter
    def DepositeCode(self, value):
        self.DepositeCode = value

    Pib = property()

    @Pib.getter
    def Pib(self):
        return self.Pib

    @Pib.setter
    def Pib(self, value):
        self.Pib = value

    DepositeSum = property()

    @DepositeSum.getter
    def DepositeSum(self):
        return self.DepositeSum

    @DepositeSum.setter
    def DepositeSum(self, value):
        self.DepositeSum = value

    DepositeEnded = property()

    @DepositeEnded.getter
    def DepositeEnded(self):
        return self.DepositeEnded

    @DepositeEnded.setter
    def DepositeEnded(self, value):
        self.DepositeEnded = value

    EmployeeCode = property()

    @EmployeeCode.getter
    def EmployeeCode(self):
        return self.EmployeeCode

    @EmployeeCode.setter
    def EmployeeCode(self, value):
        self.EmployeeCode = value

    Address = property()

    @Address.getter
    def Address(self):
        return self.Address

    @Address.setter
    def Address(self, value):
        self.Address = value

    Phone = property()
    @Phone.getter
    def Phone(self):
        return self.Phone

    @Phone.setter
    def Phone(self, value):
        self.Phone = value

    PassportData = property()

    @PassportData.getter
    def PassportData(self):
        return self.PassportData

    @PassportData.setter
    def PassportData(self, value):
        self.PassportData = value

    DepositeDate = property()
    @DepositeDate.getter
    def DepositeDate(self):
        return self.DepositeDate

    @DepositeDate.setter
    def DepositeDate(self, value):
        self.DepositeDate = value

    EndDepositeDate = property()
    @EndDepositeDate.getter
    def EndDepositeDate(self):
        return self.EndDepositeDate

    @EndDepositeDate.setter
    def EndDepositeDate(self, value):
        self.EndDepositeDate = value
