from BankDomain.Investor import Investor
from BankDomain.Currency import Currency
from BankDomain.Deposits import Deposit
from BankDomain.Role import Role
from BankDomain.Employee import Employee
from BankDomain.BankUOW import domainUOW
from BankDomain.DBInitializer import DbInitializer
from BankDomain.DAOs import EmployeeDAO

initializer = DbInitializer.inst()
initializer.CreateTables()
#initializer.CreateTables();

uow = domainUOW()
empDAO = EmployeeDAO()
inst = Employee()
inst.EmployeeCode = 20
inst.Pib = 'Kosobutskiy Bogdan'
inst.PassportData = 'Tu354352'
inst.Address = "Jitomir st."

inst.Age = 23
inst.RoleCode = 3

#uow.registerNew(inst)
#empDAO.save(inst);
insert = Employee()
insert.RoleCode = 2
insert.Pib = 'Lazuto Maxim'
insert.PassportData = 'MK233433'
insert.Address = 'Kyiv'
insert.Age = 22

delete = Employee()
delete.EmployeeCode = 5

uow.registerNew(insert)
uow.registerDeleteMark(delete)
uow.registerDirty(inst)
uow.commit()
# emp = empDAO.load({'EmployeeCode': 5})
#
# for key in Employee.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(emp, key)))
#
employeeList = empDAO.getAll()

for emp in employeeList:
    for key in Employee.__dict__.keys():
         if key[0] != '_':
            print(key + ' _ ' + str(getattr(emp, key)))
    print('------------------------------------------')

# inv = Investor()
# inv.InvestorCode = 2
# inv.load({})

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
#
# inv.load({'InvestorCode': 2})
# for key in Investor.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(inv, key)))
#
# inv.Address = """Update testing"""
# inv.Phone = """0962073633"""
# inv.PassportData = """TU3343434"""
# inv.DepositeDate = """2017.04.04"""
# inv.EndDepositeDate= """2018.04.04"""
# inv.save()
#
# inv = Investor()
# inv.load({'InvestorCode': 2})
#
# for key in Investor.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(inv, key)))


# dep = Deposit()
# dep.Title = 'UAH deposit'
# dep.MinTherm = 1
# dep.MinSum = 50000
# dep.CurrencyCode = 3
#
# dep.save()

# role = Role()
# role.Title = 'Менеджер з продаж'
# role.Duties = 'Продавати'
# role.Requirements = 'Вчасно і сумлінно виконувати роботу'
# role.Salary = 400000
# role.save()
#
# emp = Employee()
# emp.load({'EmployeeCode': 2})
#
# for key in Employee.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(emp, key)))
# emp.Pib = 'Sobko O.O.'
# emp.Age = 20
# emp.Address = 'Kyiv osokorki'
# emp.RoleCode = 3
# emp.PassportData = "PP678634"
# emp.save()
#
# role = Role()
# role.load({'RoleCode': 2})
# for key in Role.__dict__.keys():
#     if key[0] != '_':
#         print(key + ' _ ' + str(getattr(role, key)))

# curr = Currency()
# curr.Course = 1
# curr.Title = 'UAH'
# curr.save()

#inv.InvestorCode += 3
#print(str(inv.InvestorCode) + '-' + inv.Pib)

