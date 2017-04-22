from BankDomain.AbstractActiveRecordModel import AbstractARModel
from BankDomain.DBInitializer import DbInitializer


class Role(AbstractARModel):
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


    def load(self, paramDict):
        query = """SELECT """
        for key in Role.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Roles WHERE "
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
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(self, key, valueOfCell)
                    attrCounter += 1
        else:
            print("Row is not exist")

    def save(self):
        print('insert')
        if self.RoleCode == 0:
            query = """INSERT INTO Roles ("""
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
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
        query = """DELETE FROM Roles WHERE RoleCode="""
        query += str(self.RoleCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self):
        print('update')
        query = """UPDATE Roles SET """
        for key in Role.__dict__.keys():
            if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(self, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """RoleCode = """ + str(self.RoleCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)