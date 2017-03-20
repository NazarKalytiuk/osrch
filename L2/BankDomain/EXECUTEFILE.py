from BankDomain.Investor import Investor
from BankDomain.DBInitializer import DbInitializer

initializer = DbInitializer.inst()

initializer.CreateTables();

inv = Investor()
inv.InvestorCode = 1
inv.Pib = '''Sergiy Romanchuk Anat'''

inv.InvestorCode += 3
print(str(inv.InvestorCode) + '-' + inv.Pib)

