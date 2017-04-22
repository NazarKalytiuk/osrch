from BankDomain.Investor import Investor
from BankDomain.Currency import Currency
from BankDomain.Deposits import Deposit
from BankDomain.Role import Role
from BankDomain.Employee import Employee

from BankDomain.DBInitializer import DbInitializer

class EmployeeDAO(object):
    __employees = []

    @property
    def Employees(self):
        return self.__employees

    def getAll(self):
        query = """SELECT """
        for key in Employee.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Employees"
        print(query)
        resultRows = DbInitializer.inst().ExecAndReturn(query)
        if resultRows is not None:
            for resultRow in resultRows:
                attrCounter = 0
                currentEntity = Employee()
                for key in Employee.__dict__.keys():
                    if key[0] != '_' and key not in ['load', 'save', 'delete']:
                        valueOfCell = str(resultRow[attrCounter])
                        setattr(currentEntity, key, valueOfCell)
                        attrCounter += 1
                self.Employees.append(currentEntity)
            return self.Employees
        else:
            print("Rows is not exist")

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
        resultRow = DbInitializer.inst().ExecAndReturn(query)[0]
        if resultRow is not None:
            attrCounter = 0
            rowInstance = Employee()
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(rowInstance, key, valueOfCell)
                    attrCounter += 1
            return rowInstance
        else:
            print("Row is not exist")

    def save(self, instanceToSave):
        print('insert')
        if instanceToSave.EmployeeCode == 0:
            query = """INSERT INTO Employees ("""
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Employee.__dict__.keys():
                if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
                    query += '\'' + str(getattr(instanceToSave, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update(instanceToSave)

    def delete(self, instance):
        print('delete')
        query = """DELETE FROM Employees WHERE EmployeeCode="""
        query += str(instance.EmployeeCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self, instanceToUpdate):
        print('update')
        query = """UPDATE Employees SET """
        for key in Employee.__dict__.keys():
            if key[0] != '_' and key not in ['EmployeeCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(instanceToUpdate, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """EmployeeCode = """ + str(instanceToUpdate.EmployeeCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)



class InvestorDAO(object):
    __entities = []

    @property
    def Entities(self):
        return self.__entities

    def getAll(self):
        query = """SELECT """
        for key in Investor.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Investors"
        print(query)
        resultRows = DbInitializer.inst().ExecAndReturn(query)
        if resultRows is not None:
            for resultRow in resultRows:
                attrCounter = 0
                currentEntity = Investor()
                for key in Investor.__dict__.keys():
                    if key[0] != '_' and key not in ['load', 'save', 'delete']:
                        valueOfCell = str(resultRow[attrCounter])
                        setattr(currentEntity, key, valueOfCell)
                        attrCounter += 1
                self.Entities.append(currentEntity)
            return self.Entities
        else:
            print("Rows is not exist")

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
            return self.getAll()
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
            rowEntity = Investor()
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(rowEntity, key, valueOfCell)
                    attrCounter += 1
            return rowEntity
        else:
            print("Row is not exist")

    def save(self, entity):
        print('insert')
        if entity.InvestorCode == 0:
            query = """INSERT INTO Investors ("""
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Investor.__dict__.keys():
                if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                    query += '\'' + str(getattr(entity, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update(entity)

    def delete(self, entity):
        print('delete')
        query = """DELETE FROM Investors WHERE InvestorCode="""
        query += str(entity.InvestorCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self, entity):
        print('update')
        query = """UPDATE Investors SET """
        for key in Investor.__dict__.keys():
            if key[0] != '_' and key not in ['InvestorCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(entity, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """InvestorCode = """ + str(entity.InvestorCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)


class DepositDAO(object):
    __entities = []

    @property
    def Entities(self):
        return self.__entities

    def getAll(self):
        query = """SELECT """
        for key in Deposit.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Deposits"
        print(query)
        resultRows = DbInitializer.inst().ExecAndReturn(query)
        if resultRows is not None:
            for resultRow in resultRows:
                attrCounter = 0
                currentEntity = Deposit()
                for key in Deposit.__dict__.keys():
                    if key[0] != '_' and key not in ['load', 'save', 'delete']:
                        valueOfCell = str(resultRow[attrCounter])
                        setattr(currentEntity, key, valueOfCell)
                        attrCounter += 1
                self.Entities.append(currentEntity)
            return self.Entities
        else:
            print("Rows is not exist")


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
            entity = Deposit()
            for key in Deposit.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(entity, key, valueOfCell)
                    attrCounter += 1
            return entity
        else:
            print("Row is not exist")

    def save(self, entity):
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
                    query += '\'' + str(getattr(entity, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update(entity)

    def delete(self, entity):
        print('delete')
        query = """DELETE FROM Deposits WHERE DepositeCode="""
        query += str(entity.DepositeCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self,entity):
        print('update')
        query = """UPDATE Deposits SET """
        for key in Deposit.__dict__.keys():
            if key[0] != '_' and key not in ['DepositeCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(entity, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """DepositeCode = """ + str(entity.DepositeCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)



class CurrencyDAO(object):
    __entities = []

    @property
    def Entities(self):
        return self.__entities

    def getAll(self):
        query = """SELECT """
        for key in Currency.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Currencies"
        print(query)
        resultRows = DbInitializer.inst().ExecAndReturn(query)
        if resultRows is not None:
            for resultRow in resultRows:
                attrCounter = 0
                currentEntity = Currency()
                for key in Currency.__dict__.keys():
                    if key[0] != '_' and key not in ['load', 'save', 'delete']:
                        valueOfCell = str(resultRow[attrCounter])
                        setattr(currentEntity, key, valueOfCell)
                        attrCounter += 1
                self.Entities.append(currentEntity)
            return self.Entities
        else:
            print("Rows is not exist")


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
        resultRow = DbInitializer.inst().ExecAndReturn(query)[0]
        if resultRow is not None:
            attrCounter = 0
            entity = Currency()
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(entity, key, valueOfCell)
                    attrCounter += 1
            return entity
        else:
            print("Row is not exist")

    def save(self, entity):
        print('insert')
        if entity.CurrencyCode == 0:
            query = """INSERT INTO Currencies ("""
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Currency.__dict__.keys():
                if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
                    query += '\'' + str(getattr(entity, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update(entity)

    def delete(self,entity):
        print('delete')
        query = """DELETE FROM Currencies WHERE CurrencyCode="""
        query += str(entity.CurrencyCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self,entity):
        print('update')
        query = """UPDATE Currencies SET """
        for key in Currency.__dict__.keys():
            if key[0] != '_' and key not in ['CurrencyCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(entity, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """CurrencyCode = """ + str(entity.CurrencyCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)


class RoleDAO(object):
    __entities = []

    @property
    def Entities(self):
        return self.__entities

    def getAll(self):
        query = """SELECT """
        for key in Currency.__dict__.keys():
            if key[0] != '_' and key not in ['load', 'save', 'delete']:
                query += key
                query += ','
        query = query[:-1]
        query += " FROM Roles"
        print(query)
        resultRows = DbInitializer.inst().ExecAndReturn(query)
        if resultRows is not None:
            for resultRow in resultRows:
                attrCounter = 0
                currentEntity = Role()
                for key in Role.__dict__.keys():
                    if key[0] != '_' and key not in ['load', 'save', 'delete']:
                        valueOfCell = str(resultRow[attrCounter])
                        setattr(currentEntity, key, valueOfCell)
                        attrCounter += 1
                self.Entities.append(currentEntity)
            return self.Entities
        else:
            print("Rows is not exist")


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
            entity = Role()
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['load', 'save', 'delete']:
                    valueOfCell = str(resultRow[attrCounter])
                    setattr(entity, key, valueOfCell)
                    attrCounter += 1
            return entity
        else:
            print("Row is not exist")

    def save(self, entity):
        print('insert')
        if entity.RoleCode == 0:
            query = """INSERT INTO Roles ("""
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
                    query += key
                    query += ','
            query = query[:-1]
            query += """) VALUES ("""
            for key in Role.__dict__.keys():
                if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
                    query += '\'' + str(getattr(entity, key)) + '\''
                    query += ','
            query = query[:-1]
            query += ')'
            print(query)
            DbInitializer.inst().ExecQuery(query)
        else:
            self._update(entity)

    def delete(self, entity):
        print('delete')
        query = """DELETE FROM Roles WHERE RoleCode="""
        query += str(entity.RoleCode)
        DbInitializer.inst().ExecQuery(query)

    def _update(self, entity):
        print('update')
        query = """UPDATE Roles SET """
        for key in Role.__dict__.keys():
            if key[0] != '_' and key not in ['RoleCode', 'load', 'save', 'delete']:
                param = key + '=' + '\'' + str(getattr(entity, key)) + '\''
                query += param
                query += ','
        query = query[:-1]
        whereParam = """RoleCode = """ + str(entity.RoleCode)
        query += """WHERE """ + whereParam
        print(query)
        DbInitializer.inst().ExecQuery(query)