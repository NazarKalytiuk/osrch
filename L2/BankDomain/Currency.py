class Currency(object):
    CurrencyCode = property()

    @CurrencyCode.getter
    def CurrencyCode(self):
        return self.CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, value):
        self.CurrencyCode = value

    Title = property()

    @Title.getter
    def Title(self):
        return self.Title

    @Title.setter
    def Title(self, value):
        self.Title = value

    Course = property()
    @Course.getter
    def Course(self):
        return self.Course

    @Course.setter
    def Course(self, value):
        self.Course = value