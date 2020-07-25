from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(blank = False, max_length = 20)
    lastname = models.CharField(blank = False, max_length = 20)
    college = models.CharField(blank = False, max_length = 50)
    branch = models.CharField(blank = False, max_length = 50)
    year = models.CharField(blank = False, max_length = 20)
    email = models.EmailField(blank = False)
    password = models.CharField(blank = False, max_length = 20)
    confirmpassword = models.CharField(blank=False, max_length = 20)

    def __str__(self):
        return self.username

