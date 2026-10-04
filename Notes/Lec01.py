#First we created a polls app in django by running
# python manage.py startapp polls

# NOw we wrote our first ever view :-

from django.http import HttpResponse


def index(request): #request:- parameter (user ne jo kuch manga yni browser se aaya data )(in simple words ye ek object hai jiske andar wo saari details hongi jaise browser se aaya data browser ke dwara bheji gayi request )

    return HttpResponse("Hello, world. You're at the polls index.")  #REsponse which we are sending back 

# What is a view?
# View ek Python function hai jo browser ki request leta hai aur response wapas deta hai.

#Problem :- view to bana diya lekin how will browser know ki kaunse URL pe view ko chalana hai ??

#That's whyy humko ek URLconf chahiye 
#YE ek urls.py file hoti hai jo batati hai ki is url pe aaye to ye view chalao 
# Simple example: Reception ka directory board

# URL = room number
# View = us room me baitha banda
# urls.py = board jo batata hai kaunsa number kahan jaata hai

from django.urls import path
# Ye Django ke urls module se path function import kar raha hai.

# path() ka kaam hai URL ko kisi view/function ke saath connect karna.

from . import views #.(dot) ka matlab current directory ya package main se 

urlpatterns = [  #"Kaunsa URL hit hone par kaunsa function execute karna hai?"
    
    #Even simple language "Meri website ke URLs ki list."
    path("", views.index, name="index"),

    #This structure resemble what path() function needs(URL,VIEW,NAME)

    #""(empty string) yni website ka home page ka url 
    #Views.index means views ke andar ke index function ko use karo 
    # name="index"    → is URL ko hum kya naam se bula sakte hain?

]

#AB pata chal gya ki polls ke andar empty url aaye to views.index chalao 
# Lekin Django ko ye pata hi nahi ki polls/urls.py naam ki koi file hai.

# Django sabse pehle main mysite/urls.py dekhta hai.

# Isliye hume main URL file mein batana padega:"Bhai, agar URL /polls/ se start ho raha hai, toh aage ka kaam polls/urls.py ko de dena."

from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("polls/",include("polls.urls")),
    path('admin/', admin.site.urls),
    
]
#What is include :-include() Django ka ek function hai.

# Iska kaam:"Is URL ke aage ka kaam kisi doosri urls.py file ko de do."