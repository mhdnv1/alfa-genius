from django.urls import path
from .views import *

urlpatterns = [
    path('' , index, name='index'),
    path('category/<int:category_id>/', category , name='category'),
    path('header/' , header, name='header'),
    path('contact/' , contact, name='contact'),
    path('exam/' , exam, name='exam'),
    path('about/' , about, name='about'),
    path('news/' , news, name='news'),
    path('evant/' , evant, name='evant'),
    path('services/' , services, name='services'),
    path('teachers/' , teachers, name='teachers'),
    path('exem/<int:id>' , getIdexamcard , name="exem_card"),
    path('evant/<int:id>' , getIdevantcard , name="evant_card"),
    path('new/<int:id>' , getIdnewcard , name="new_card"),
]