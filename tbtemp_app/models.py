from django.db import models

# Create your models here.
class Student(models.Model):
    fullName = models.CharField(blank = False, max_length = 20)
    college = models.CharField(blank = False, max_length = 50)
    branch = models.CharField(blank = False, max_length = 50)
    year = models.CharField(blank = False, max_length = 20)
    email = models.EmailField(blank = False)
    password = models.CharField(blank = False, max_length = 20)
    confirmPassword = models.CharField(blank=False, max_length = 20)

    def __str__(self):
        return self.fullName

class Subject(models.Model):
    name = models.CharField(blank = False, max_length = 30)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(blank = False, max_length = 50)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = "Topic")

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(blank = False, max_length = 20)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Activity")
    files = models.FileField()

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(blank = False, max_length = 50)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Document")
    files = models.FileField()

    def __str__(self):
        return self.name

class StudentUpload(models.Model):
    STUDENT_UPLOAD_STATUS=(
        ('approved','approved'),
        ('uploaded','uploaded'),
    )
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "StudentUpload")
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "StudentUpload")
    files = models.FileField()
    status = models.CharField(max_length = 20, choices = STUDENT_UPLOAD_STATUS)
    name = models.CharField(blank = False, max_length = 20)

    def __str__(self):
        return self.name


