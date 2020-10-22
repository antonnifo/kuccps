from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    
    user     = models.OneToOneField(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    index    = models.IntegerField()
    school   = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    points   = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username


class Institution(models.Model):

    TYPE_CHOICES = (
        ("Private", "Private"),
        ("Public", "Public"),
    )

    CATEGORY_CHOICES = (
        ("University", "University"),
        ("TVET Colleage", "TVET Colleage"),
    )

    name  = models.CharField(max_length=200)
    typ   = models.CharField(max_length=50, choices=TYPE_CHOICES)
    key   = models.CharField(max_length=200)
    city  = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  

    def __str__(self):
        return self.name


class Programme(models.Model):
    
    CATEGORY_CHOICES  = (
            ("Degree","Degree"),
            ("Diploma","Diploma"),                  
            ("Certificate","Certificate"),                  
                 
        )
    name     = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    students = models.ManyToManyField(Student, through='Enrollment')
    institution = models.ManyToManyField(Institution, through='ProgrammeChoice')

    def __str__(self):
        return self.name


class ProgrammeChoice(models.Model):
     programme   = models.ForeignKey(Programme, on_delete=models.CASCADE)
     institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
     cutoff_points = models.DecimalField(max_digits=10, decimal_places=2)
     

class Enrollment(models.Model):

    Student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['Student', 'programme', 'institution']]
    


