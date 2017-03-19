class Deposit(object):
    DepositeCode = property()
    @DepositeCode.getter
    def DepositeCode(self):
        return self.DepositeCode
    @DepositeCode.setter
    def DepositeCode(self, value):
        self.DepositeCode = value

    Title = property()
    @Title.getter
    def Title(self):
        return self.Title
    @Title.setter
    def Title(self, value):
        self.Title = value

    MinTherm = property()

    @MinTherm.getter
    def MinTherm(self):
        return self.MinTherm

    @MinTherm.setter
    def MinTherm(self, value):
        self.MinTherm = value

    MinSum = property()

    @MinSum.getter
    def MinSum(self):
        return self.MinSum

    @MinSum.setter
    def MinSum(self, value):
        self.MinSum = value

    CurrencyCode = property()

    @CurrencyCode.getter
    def CurrencyCode(self):
        return self.CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, value):
        self.CurrencyCode = value

    AdditionalCondition = property()

    @AdditionalCondition.getter
    def AdditionalCondition(self):
        return self.AdditionalCondition

    @AdditionalCondition.setter
    def AdditionalCondition(self, value):
        self.AdditionalCondition = value