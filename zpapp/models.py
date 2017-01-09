from django.db import models
import datetime


class Worker (models.Model):
    name = models.CharField ('Name', max_length=30)
    surname = models.CharField ('Surname', max_length=30)
    patronymic = models.CharField ('Patronymic', max_length=30)
    address = models.CharField ('Address', max_length=100)
    index = models.CharField ('Index', max_length=6)
    tel = models.CharField ('Phone number', unique=True,  max_length=15)
    ip_number = models.CharField ('ID number', unique=True,  max_length=12 )
    score_number = models.CharField ('Score number', unique=True,  max_length=14)
    mfo = models.CharField ('MFO', max_length=6 )
    contract = models.CharField ('Contract №', unique=True, max_length=30)
    date_contract = models.DateTimeField('Contract Date', default= datetime.datetime.utcnow())

    def __str__(self):
        return self.surname


class Salary (models.Model):
    worker = models.ForeignKey(Worker)
    salary_uah = models.IntegerField ('Salary')
    date = models.DateTimeField('Date', default=datetime.datetime.utcnow())

    def __str__(self):
        return self.worker.surname
