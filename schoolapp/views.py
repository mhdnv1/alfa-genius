from django.shortcuts import render , redirect
from .models import *

# from django.shortcuts import render, redirect
# from .models import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate


# Create your views here.

def header(request):
    logo = Logo.objects.all()
    context = {
        'logo':logo,
    }
    return render(request , 'header.html' , context)

def about(request):
    logo = Logo.objects.all()
    text = About_text.objects.all()
    image = About_image.objects.all()
    context = {
        'logo':logo,
        'text':text,
        'image':image,

    }
    return render(request , 'about.html' , context)

def index(request):
    carusel_main = Carusel_main.objects.all()
    carusel = Carusel.objects.all()
    lavita = Lavita_p.objects.all()
    logo = Logo.objects.all()
    year = Course_year.objects.all()
    course_category = Course_category.objects.all()
    course = Course.objects.all()
    exam = Exam.objects.all()
    event = Event.objects.all()
    new = New.objects.all()
    category = Course_category.objects.all()
    context = {
        'carusel_main':carusel_main,
        'carusel':carusel,
        'lavita':lavita,
        'logo':logo,
        'year':year,
        'course_category':course_category,
        'course':course,
        'exam':exam,
        'event':event,
        'new':new,
        'category':category,

    }
    return render(request , 'index.html' , context)

def evant(request):
    logo = Logo.objects.all()
    event = Event.objects.all()
    context = {
        'logo':logo,
        'event':event,
    }
    return render(request , 'evant.html' , context)

def news(request):
    logo = Logo.objects.all()
    new = New.objects.all()
    context = {
        'logo':logo,
        'new':new,
    }
    return render(request , 'news.html' , context)

def contact(request):
    logo = Logo.objects.all()
    work_day = Work_day.objects.all()
    grafic = Grafic.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context = {
        'logo':logo,
        'work_day':work_day,
        'grafic':grafic,
        'phone':phone,
        'email':email,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('c_email')
        phone = request.POST.get('phone')
        massage = request.POST.get('massage')
        contact = Contacts.objects.create(
            email = email,
            phone = phone,
            massage = massage,
            name = name,
        )
        contact.save()
    return render(request , 'contact.html' , context)

def exam(request):
    logo = Logo.objects.all()
    exem_text = Exem_text.objects.all()
    exem_text_3 = Exem_text_3.objects.all()
    exem_level = Exem_level.objects.all()
    exem_photo = Exem_photo.objects.all()
    context = {
        'logo':logo,
        'exem_text':exem_text,
        'exem_text_3':exem_text_3,
        'exem_level':exem_level,
        'exem_photo':exem_photo,
    }
    return render(request , 'exam.html' , context)

def services(request):
    logo = Logo.objects.all()
    service_photo = Service_photo.objects.all()
    service_text = Service_text.objects.all()
    context = {
        'logo':logo,
        'service_photo':service_photo,
        'service_text':service_text,
    }
    return render(request , 'services.html' , context)

def teachers(request):
    logo = Logo.objects.all()
    teachers = Teachers.objects.all()
    students = Students.objects.all()
    context = {
        'logo':logo,
        'teachers':teachers,
        'students':students,
    }
    return render(request , 'teachers.html' , context)

def category(request , category_id):
    course = Course.objects.filter(category_id = category_id)
    category = Course_category.objects.all()
    categories = Course_category.objects.get(id = category_id)
    course_year = Course_year.objects.all
    context = {
        'course':course,
        'category':category,
        'categories':categories,
        'course_year':course_year,
    }
    return render(request , 'category.html' , context)


def getIdexamcard(request, id):
    exam = Exam.objects.get(id = id)
    logo = Logo.objects.all()
    context={
        "exam":exam,
        "logo":logo
    }
    return render(request, 'exem_card.html', context)

def getIdevantcard(request, id):
    evant = Event.objects.get(id = id)
    logo = Logo.objects.all()
    context={
        "evant":evant,
        "logo":logo
    }
    return render(request, 'evant_card.html', context)

def getIdnewcard(request, id):
    new = New.objects.get(id = id)
    logo = Logo.objects.all()
    context={
        "new":new,
        "logo":logo
    }
    return render(request, 'news_card.html', context)

