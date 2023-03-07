from django.db import models


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    chat_id = models.IntegerField()
    status_name = models.CharField(max_length=20)
    curator = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    status_name = models.CharField(max_length=20)






