import sqlite3


class DbInitializer(object):
    __instance = None

    @staticmethod
    def inst():
        if DbInitializer.__instance == None:
            DbInitializer.__instance = DbInitializer()
        return DbInitializer.__instance

    def Connect(self):
        conn = sqlite3.connect('Bank.db')
        return conn

    def CreateTables(self):
        dbConnection = self.Connect()
        dbConnection.execute('''CREATE TABLE Employees (
	EmployeeCode INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Pib TEXT NOT NULL,
	Age INTEGER NOT NULL,
	Address TEXT NOT NULL,
	PassportData TEXT NOT NULL,
	RoleCode INT NOT NULL
)
''')
        dbConnection.execute('''CREATE TABLE Roles (
	RoleCode INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Title TEXT NOT NULL,
	Salary INTEGER NOT NULL,
	Duties TEXT NOT NULL,
	Requirements TEXT NOT NULL
)''')
        dbConnection.execute('''CREATE TABLE Deposits (
	DepositeCode INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Title TEXT NOT NULL,
	MinTherm INTEGER NOT NULL,
	MinSum INTEGER NOT NULL,
	CurrencyCode INTEGER NOT NULL,
	AdditionalCondition TEXT NOT NULL
)''')
        dbConnection.execute('''CREATE TABLE Currencies (
	CurrencyCode INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Title TEXT NOT NULL,
	Course REAL NOT NULL
)''')
        dbConnection.execute('''
CREATE TABLE Investors (
	InvestorCode INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	PIB TEXT NOT NULL,
	DepositeCode INTEGER NOT NULL,
	DepositeSum INTEGER NOT NULL,
	DepositeEnded INTEGER NOT NULL,
	EmployeeCode INTEGER NOT NULL,
	Address TEXT NOT NULL,
	Phone TEXT NOT NULL,
	PassportData TEXT NOT NULL,
	DepositeDate TEXT NOT NULL,
	EndDepositeDate TEXT NOT NULL
)''')
        dbConnection.close()

    def ExecQuery(self, query):
        dbConnection = self.Connect()
        dbConnection.execute(query)
        dbConnection.commit()
        dbConnection.close()

    def ExecAndReturn(self, query):
        dbConnection = self.Connect()
        result = dbConnection.execute(query).fetchone()
        dbConnection.close()
        return result