from BankDomain.AbstractActiveRecordModel import AbstractARModel
from BankDomain.DBInitializer import DbInitializer


class Employee(AbstractARModel):
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

    __PassportData = ''

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


    def load(self, paramDict):
        query = """SELECT """
        for key in Employee.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Employees WHERE "
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
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(self, key, valueOfCell)
                    attrCounter += 1
        else:
            print("Row is not exist")

    def save(self):
        print('insert')
        if self.EmployeeCode == 0:
            query = """INSERT INTO Employees ("""
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
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
        query = """DELETE FROM Employees WHERE EmployeeCode="""
        query += str(self.EmployeeCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self):
        print('update')
        query = """UPDATE Employees SET """
        for key in Employee.__dict__.keys():
            if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(self, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """EmployeeCode = """ + str(self.EmployeeCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)