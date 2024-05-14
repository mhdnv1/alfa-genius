from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Logo(models.Model):
    logo = models.CharField(max_length=50 , blank=True)
    image = models.ImageField()
    def __str__(self):
        return self.logo
    
class Carusel_main(models.Model):
    title = models.CharField(max_length=150 ,  default='Default Title')
    image = models.ImageField()
    carusel_p = models.CharField(max_length=250 , blank=True)
    def __str__(self):
        return self.title


class Carusel(models.Model):
    title = models.CharField(max_length=50 , blank=True)
    image = models.ImageField()
    carusel_p = models.CharField(max_length=250 , blank=True)
    def __str__(self):
        return self.title
    
class Lavita_p(models.Model):
    title = models.CharField(max_length=50 , blank=True)
    h1 = models.CharField(max_length=20 , blank=True )
    text = models.TextField(max_length=500)
    def __str__(self):
        return self.title

class Course_year(models.Model):
    title = models.CharField(max_length=50 , blank=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class Course_category(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(Course_category , on_delete=models.CASCADE)
    years = models.CharField(max_length=15)
    how_many_lesson_in_week = models.CharField(max_length=15)
    how_many_hour = models.CharField(max_length=15)
    lesson_start = models.CharField(max_length=15)
    lesson_finish = models.CharField(max_length=15)
    cost = models.CharField(max_length=30)
    cost_hour = models.CharField(max_length=30 , default='Default Title')
    how_many_lesson_in_month = models.CharField(max_length=15)
    how_many_pay = models.CharField(max_length=30)
    course_p = models.CharField(max_length=200)
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title

class Exam(models.Model):
    title = models.CharField(max_length=150)
    exams_h1 = models.CharField(max_length=100)
    image = models.ImageField()
    exam_li1 = models.CharField(max_length=200 , blank=True)
    exam_li2 = models.CharField(max_length=200 , blank=True)
    exam_li3 = models.CharField(max_length=200 , blank=True)
    description = models.TextField(default=' ')
    def __str__(self):
        return self.title
    
    

class Event(models.Model):
    title = models.CharField(max_length=150)
    events_h1 = models.CharField(max_length=100)
    events_p = models.CharField(max_length=1000)
    image = models.ImageField()
    description = models.TextField(default=' ')
    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=150)
    news_h1 = models.CharField(max_length=100)
    news_p = models.CharField(max_length=1000)
    description = models.TextField(default=' ')

    def __str__(self):
        return self.title

class Service_photo(models.Model):
    image = models.ImageField()

class Service_text(models.Model):
    service_h1 = models.CharField(max_length=150)
    service_text = models.TextField()
    service_text_2 = models.TextField(blank=True)
    service_text_in_red =  models.CharField(max_length=300)

class Exem_photo(models.Model):
    image = models.ImageField()

class Exem_text(models.Model):
    exam_text_1 = models.TextField()
    exam_text_2 = models.TextField()
    exam_text_3 = models.TextField()
    exam_text_4 = models.TextField()

class Exem_text_3(models.Model):
    exam_text_3 = models.TextField()

class Exem_level(models.Model):
    level = models.CharField(max_length=30)
    words = models.CharField(max_length=30)
    minute = models.CharField(max_length=30)
    level_for_study = models.CharField(max_length=30)
    balls = models.CharField(max_length=30)
    all_balls = models.CharField(max_length=30)

class Work_day(models.Model):
    days = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    dont_work_days = models.CharField(max_length=100 , default='ВС')


class Grafic(models.Model):
    day = models.CharField(max_length=50)
    in_which_times = models.CharField(max_length=100)

class Phone(models.Model):
    phone_number = models.CharField(max_length=50)

class Email(models.Model):
    whose_email = models.CharField(max_length=200)
    email_adress = models.CharField(max_length=100)


class Teachers(models.Model):
    name = models.CharField(max_length=150)
    paragraf = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.name
    
class Students(models.Model):
    name = models.CharField(max_length=150)
    paragraf = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length=255 , blank=True)
    email = models.EmailField(max_length=255, unique=True) 
    phone = models.CharField(max_length=255)
    massage = models.TextField()
    def __str__(self):
        return self.email


class About_text(models.Model):
    tag = models.CharField(max_length=155 , blank=True)
    text = models.TextField()
    def __str__(self):
        return self.tag
    
class About_image(models.Model):
    name = models.CharField(max_length=155 , blank=True)
    image = models.ImageField()
    def __str__(self):
        return self.name