from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.



class user_type(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_teach = models.BooleanField(default= True)



class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cg = models.IntegerField(default = 0)




class teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)





class courses(models.Model):
    credit = models.IntegerField(default = 5)
    name = models.CharField(max_length=1000,unique=True)
    Inf = models.CharField(max_length = 1000)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)

# Create your models here.


class sc(models.Model):
    stud = models.ForeignKey(student, null=True ,on_delete=models.CASCADE)
    course = models.ForeignKey(courses , null=True, on_delete=models.CASCADE)
    grade = models.IntegerField(default = 0)
    date = models.DateField(student, default= datetime.date.today())
    time = models.TimeField(default=datetime.datetime.now().time())


class message(models.Model):
    subject = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.datetime.now().time())
    msg = models.CharField(max_length=1000)
    course = models.ForeignKey(courses , null=True, on_delete=models.CASCADE)
