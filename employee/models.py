from django.db import models


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.status_name}"

    class Meta:
        db_table = "employee_status"


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, blank=False)
    firstname = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=30, unique=True, blank=False)
    phone_number = models.CharField(max_length=20, unique=True, blank=False)
    chat_id = models.IntegerField(unique=True)
    status_name = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    curator = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id}--{self.username}"

    class Meta:
        db_table = "employee_employees"
