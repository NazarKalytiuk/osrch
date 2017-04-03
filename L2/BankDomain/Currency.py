from BankDomain.AbstractActiveRecordModel import AbstractARModel
from BankDomain.DBInitializer import DbInitializer


class Currency(AbstractARModel):
    __CurrencyCode = 0

    @property
    def CurrencyCode(self):
        return self.__CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, value):
        self.__CurrencyCode = value

    __Title = ''

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, value):
        self.__Title = value

    __Course = 0.00

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        self.__Course = value


    def load(self, paramDict):
        query = """SELECT """
        for key in Currency.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Currencies WHERE "
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
        resultRow = DbInitializer.inst().ExecAndReturn(query)
        if resultRow is not None:
            attrCounter = 0
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(self, key, valueOfCell)
                    attrCounter += 1
        else:
            print("Row is not exist")

    def save(self):
        print('insert')
        if self.CurrencyCode == 0:
            query = """INSERT INTO Currencies ("""
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
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
        query = """DELETE FROM Currencies WHERE CurrencyCode="""
        query += str(self.CurrencyCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self):
        print('update')
        query = """UPDATE Currencies SET """
        for key in Currency.__dict__.keys():
            if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(self, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """CurrencyCode = """ + str(self.CurrencyCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)

