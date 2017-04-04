from BankDomain.AbstractActiveRecordModel import AbstractARModel
from BankDomain.DBInitializer import DbInitializer

class Investor(AbstractARModel):
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

    __EmployeeCode = 0

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

    __PassportData = ''

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

    def load(self, paramDict):
        query = """SELECT """
        for key in Investor.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Investors WHERE "
        equal_substr = '{attr_name} = {attr_value}'
        counter = len(paramDict)
        if counter == 0:
            paramDict = {'InvestorCode': self.InvestorCode}
            counter = 1
        for param in paramDict:
            query += equal_substr.format(attr_name=param, attr_value=paramDict[param])
            if counter == 1:
                query += ';'
            else:
                query += ' AND '
            counter -= 1
        print(query)
        resultRow = DbInitializer.inst().ExecAndReturn(query)
        if resultRow is not None:
            attrCounter = 0
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(self, key, valueOfCell)
                    attrCounter += 1
        else:
            print("Row is not exist")

    def save(self):
        print('insert')
        if self.InvestorCode == 0:
            query = """INSERT INTO Investors ("""
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                    query += '\'' + str(getattr(self, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update()

    def delete(self):
        print('delete')
        query = """DELETE FROM Investors WHERE InvestorCode="""
        query += str(self.InvestorCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self):
        print('update')
        query = """UPDATE Investors SET """
        for key in Investor.__dict__.keys():
            if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(self, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """InvestorCode = """ + str(self.InvestorCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)

