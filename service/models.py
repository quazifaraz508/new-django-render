from django.db import models
from django.contrib.auth.hashers import make_password


class Service(models.Model):
    sev_title=models.CharField(max_length=50)
    ser_dec= models.TextField()


class Signup(models.Model):
    name1=models.CharField(null=False,blank=False,max_length=100)
    email1=models.EmailField(null=True,blank=False,unique=True)
    pass1=models.CharField(null=False,blank=False,max_length=128)
    
    def save(self, *args, **kwargs):
        self.pass1 = make_password(self.pass1)
        super(Signup, self).save(*args, **kwargs)

class Register_quiz(models.Model):
    fname=models.CharField(null=False,blank=False,max_length=100)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    
    fname2=models.CharField(null=False,blank=False,max_length=100)
    GENDER_CHOICES2 = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender2 = models.CharField(max_length=10, choices=GENDER_CHOICES2, null=False, blank=False)
    birthday2 = models.DateField(null=False, blank=False)
    
    fname3=models.CharField(null=False,blank=False,max_length=100)
    GENDER_CHOICES3 = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender3 = models.CharField(max_length=10, choices = GENDER_CHOICES3, null=False, blank=False)
    birthday3 = models.DateField(null=False, blank=False)
    Collage_chose=(
        ('Anjuman Engg', 'Anjuman Engg'),
        ('Anjuman Poly', 'Anjuman Poly'),
        ('Other', 'Other'),
    )
    # Collage=models.CharField(max_length=100,choices= Collage_chose,blank=False)
    Collage=models.CharField(max_length=100, choices =  Collage_chose, null=True, blank=True)
    
    Contact_no=models.CharField(max_length=10,null=False,blank=False)
    
