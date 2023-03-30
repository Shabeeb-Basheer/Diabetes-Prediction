from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class expert(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    email = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

class user(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    email = models.CharField(max_length=100)

class complaint(models.Model):
    uid = models.ForeignKey(user,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100)

class notification(models.Model):
    notification = models.CharField(max_length=100)
    date = models.DateField()

class tips(models.Model):
    eid = models.ForeignKey(expert, on_delete=models.CASCADE)
    tips = models.CharField(max_length=100)
    date = models.DateField()

class doubt(models.Model):
    eid = models.ForeignKey(expert, on_delete=models.CASCADE)
    uid = models.ForeignKey(user, on_delete=models.CASCADE)
    doubt = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100)
