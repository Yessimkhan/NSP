from django.db import models


class Employees(models.Model):
    full_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    date_of_receipt = models.DateField()
    salary = models.IntegerField()
    head = models.IntegerField()

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.full_name


