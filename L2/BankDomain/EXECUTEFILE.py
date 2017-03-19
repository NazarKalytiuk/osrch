from BankDomain.Investor import Investor

inv = Investor()
inv.InvestorCode = 1
inv.Pib = '''Sergiy Romanchuk Anat'''

inv.InvestorCode += 3
print(str(inv.InvestorCode) + '-' + inv.Pib)