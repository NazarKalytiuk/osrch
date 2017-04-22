from BankDomain.Investor import Investor
from BankDomain.Currency import Currency
from BankDomain.Deposits import Deposit
from BankDomain.Role import Role
from BankDomain.Employee import Employee

from BankDomain.DBInitializer import DbInitializer

class domainUOW(object):
    __objectPool = {}

    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'

    def registerNew(self, entity):
        self.__objectPool[entity] = self.newMark

    def registerClean(self, entity):
        self.__objectPool[entity] = self.cleanMark

    def registerDirty(self, entity):
        self.__objectPool[entity] = self.dirtyMark

    def registerDeleteMark(self, entity):
        self.__objectPool[entity] = self.deletedMark

    def commit(self):
        for entity in self.__objectPool:
            entityMark = self.__objectPool[entity]
            if entityMark is self.newMark:
                entity.save()
            elif entityMark is self.cleanMark:
                pass
            elif entityMark is self.dirtyMark:
                entity._update()
            elif entityMark is self.deletedMark:
                entity.delete()

    def rollback(self):
        self.__objectPool.clear()