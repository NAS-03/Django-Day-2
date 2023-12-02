from django.db import models

class studentdetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    grade = models.IntegerField()
    faculty = models.CharField(max_length=50)