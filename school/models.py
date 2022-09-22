from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + '  ==>>  ' + self.cl + ' ' + 'level'



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)
    def __str__(self):
        return str(self.date) + ' ' + self.present_status



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)
    file=models.FileField()
    def __str__(self):
        return self.message + ' by ' + self.by


class Notes(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=30,null=True, default='Your Name')
    year=models.CharField(max_length=10, choices=classes, default='one')
    roll=models.CharField(max_length=10)
    message=models.CharField(max_length=500)
    file=models.FileField()
    def __str__(self):
        return self.message + ' by ' + self.by

class Grading(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=30, null=True, default='Your Name')
    student_first_name=models.CharField(max_length=30, null=True)
    student_last_name=models.CharField(max_length=30, null=True)
    roll=models.CharField(max_length=50)
    course_unit=models.CharField(max_length=100)
    assignments=models.DecimalField(max_digits=3, decimal_places=1)
    Tests=models.DecimalField(max_digits=6, decimal_places=1)
    exam=models.DecimalField(max_digits=6, decimal_places=1)

    total=models.DecimalField(max_digits=6, decimal_places=1, default='0.0')
    def save(self):
        self.total = self.assignments + self.Tests + self.exam
        return super(Grading, self).save()
    def __str__(self):
        return self.student_first_name + ' ==>> ' + self.course_unit

class Help(models.Model):
    date=models.DateField(auto_now=True)
    message=models.TextField(blank=True, max_length=1000)
    student=models.CharField(max_length=30, null=True, default='student name')
    def __str__(self):
        return self.student + ' ' + 'complaint/s'


class Test(models.Model):
    name = models.CharField(max_length=250, default='null')
    year = models.CharField(max_length=10, default='null')
    course = models.CharField(max_length=100, default='null')
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField(max_length=500)
    a = models.TextField(max_length=500, default='null')
    b = models.TextField(max_length=500, default='null')
    c = models.TextField(max_length=500, default='null')
    d = models.TextField(max_length=500, default='null')
    answer = models.CharField(max_length=5)


    def __str__(self):
        return "Question: " + self.question


class Answer(models.Model):
    student_username = models.CharField(max_length=150, default='null')
    test = models.CharField(max_length=250, default='null')
    question = models.CharField(max_length=10, default='null')
    mark = models.CharField(max_length=10, default='null')

    def __str__(self):
        return self.student_username + " => " + self.question
