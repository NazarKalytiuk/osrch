from BankDomain.AbstractActiveRecordModel import AbstractARModel
from BankDomain.DBInitializer import DbInitializer


class Deposit(AbstractARModel):
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


    def load(self, paramDict):
        query = """SELECT """
        for key in Deposit.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Deposits WHERE "
        equal_substr = '{attr_name} = {attr_value}'
        counter = len(paramDict)
        for param in paramDict:
            query += equal_substr.format(attr_name=param, attr_value=paramDict[param])
            if counter == 1:
                query += ';'
            else:
                query += ' AND '
            counter -= 1
        print(query)
        resultRow = DbInitializer.inst().ExecAndReturn(query)[0]
        if resultRow is not None:
            attrCounter = 0
            for key in Deposit.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(self, key, valueOfCell)
                    attrCounter += 1
        else:
            print("Row is not exist")

    def save(self):
        print('insert')
        if self.DepositeCode == 0:
            query = """INSERT INTO Deposits ("""
            for key in Deposit.__dict__.keys():
                if key[0] != '_' and key not in ['DepositeCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Deposit.__dict__.keys():
                if key[0] != '_' and key not in ['DepositeCode', 'load', 'save', 'delete']:
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
        query = """DELETE FROM Deposits WHERE DepositeCode="""
        query += str(self.DepositeCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self):
        print('update')
        query = """UPDATE Deposits SET """
        for key in Deposit.__dict__.keys():
            if key[0] != '_' and key not in ['DepositeCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(self, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """DepositeCode = """ + str(self.DepositeCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)