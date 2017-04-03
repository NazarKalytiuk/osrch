from BankDomain.Investor import Investor
from BankDomain.Currency import Currency
from BankDomain.Deposits import Deposit
from BankDomain.Role import Role
from BankDomain.Employee import Employee

from BankDomain.DBInitializer import DbInitializer

initializer = DbInitializer.inst()

#initializer.CreateTables();

inv = Investor()


#inv.save()
#
# for key in Investor.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(inv, key)))
#
# inv.InvestorCode = 0
# inv.Pib = '''Nazari Kalitiyk'''
# inv.InvestorCode = 0
# inv.Pib = """test adding"""
# inv.DepositeCode = 3
# inv.DepositeSum = 1000
# inv.Address = """Kyiv Borschagivka"""
#
# inv.save()
# for key in Investor.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(inv, key)))
#
# inv.InvestorCode = 0
# inv.Pib = '''Nazari Kalitiyk'''
# inv.InvestorCode = 0
# inv.Pib = """test adding"""
# inv.DepositeCode = 3
# inv.DepositeSum = 1000
# inv.Address = """Kyiv Borschagivka"""
#
# inv.save()

inv.load({'InvestorCode': 2})
for key in Investor.__dict__.keys():
    if key[0] != '_':
        print(key + ' _ ' + str(getattr(inv, key)))

inv.Address = """Up8date testing"""
inv.Phone = """0962073633"""

inv.save()

inv = Investor()
inv.load({'InvestorCode': 2})

for key in Investor.__dict__.keys():
    if key[0] != '_':
        print(key + ' _ ' + str(getattr(inv, key)))

#inv.InvestorCode += 3
#print(str(inv.InvestorCode) + '-' + inv.Pib)

