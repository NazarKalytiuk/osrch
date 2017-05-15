from django.db import models

#Create models here
#
# class A(models.Model):
#     name = models.CharField(max_length=300)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name


class Employee(models.Model):
    pib = models.CharField(max_length=300)
    role = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    requirenments = models.CharField(max_length=1000)

    def __str__(self):
        return self.pib

    def ID(self):
        return self.id


class Client(models.Model):
    pib = models.CharField(max_length=300)
    passportInfo = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    inn = models.CharField(max_length=20)

    def __str__(self):
        return self.pib

    def ID(self):
        return self.id


class Deposit(models.Model):
    employeeId = models.ForeignKey('Employee')
    clientId = models.ForeignKey('Client')

    CURRENCIES_SOURCE = (
        ('UAH', 'Hryvnia'),
        ('USD', 'Dollar USA'),
        ('EUR', 'Euro'),
        ('RUB', 'Russian ruble'),
    )
    currency = models.CharField(max_length=3,
                                      choices=CURRENCIES_SOURCE,
                                      default='UAH')

    sum = models.DecimalField(max_digits=10, decimal_places=2)
    periodDays = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    persent = models.DecimalField(max_digits=4, decimal_places=3)

    isClosed = models.NullBooleanField()
