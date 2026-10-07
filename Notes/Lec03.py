# Tumne polls/models.py mein models bana diye:

# Question
# Choice

# Lekin Django ko abhi tak officially nahi pata ki polls app project ka part hai.

# Isliye mysite/settings.py mein:

# INSTALLED_APPS = [
#     "polls.apps.PollsConfig",
#     ...
# ]

# polls.apps.PollsConfig ka matlab
# polls
#   ↓
# apps.py
#   ↓
# PollsConfig

# Matlab:

# "Django, mere project mein polls app installed/active hai."

#NOw  we can make migratiuons so run command 
# python manage.py makemigrations polls 

#What it will do ?
# Django dekhega ki models.py mein:
# Question model bana
# Choice model bana

# Aur phir ek migration file banayega:

# polls/
# └── migrations/
#     └── 0001_initial.py

# Ye file basically Django ke liye instructions/blueprint hai:

# "Database mein Question aur Choice ke tables create karne hain." Abhi database mein tables create nahi hue.Sirf migration file bani hai.

#NOw run command python manage.py migrate  
#ISse hoga ye ki django will read migration file and make change in DB 
# models.py
#    ↓
# makemigrations
#    ↓
# 0001_initial.py
#    ↓
# migrate
#    ↓
# DATABASE
#    ↓
# Question & Choice tables

# django_migrations kya hai?

# Django database mein ek special table rakhta hai:

# django_migrations

# Isme Django track karta hai:

# Kaunsi migrations already database par apply ho chuki hain?

# For example:

# 0001_initial    ✅ applied
# 0002_add_age    ❌ not applied

# Isliye migrate ko pata hota hai ki kya already ho chuka hai aur kya pending hai.

#But what will happen if i introduce somme change in existing models  models ?

#Suppose author =models.CharField(max_length=100) field aad ki Question model main toh ab phir yehi process repaet karunga 

# makemigrations-->new migration file-->migrate-->DB Update

# Purana database delete karne ki zarurat nahi.

# Isi wajah se migrations powerful hain — existing data ko preserve karte hue database structure ko update kar sakte ho.

# ============================================================
# DJANGO DATABASE API - BEGINNER NOTES
# Based on Django Tutorial 2 - "Playing with the API"
# ============================================================

# ------------------------------------------------------------
# 1. DJANGO PYTHON SHELL
# ------------------------------------------------------------

# Django project ke root folder mein ye command run karo:
#
# python manage.py shell
#
# Simple "python" command ke bajay "python manage.py shell"
# use karne ka reason:
#
# manage.py automatically DJANGO_SETTINGS_MODULE set karta hai.
#
# DJANGO_SETTINGS_MODULE Django ko batata hai ki project ki
# settings.py file kahan hai.
#
# Example:
#
# DJANGO_SETTINGS_MODULE = "mysite.settings"
#
# Iske through Django ko pata chalta hai:
# - Database configuration kya hai
# - INSTALLED_APPS kya hain
# - Time zone kya hai
# - Other Django settings kya hain
#
# Django shell start hone ke baad hum models ke saath directly
# Python mein kaam kar sakte hain.


# ------------------------------------------------------------
# 2. MODELS KO SHELL MEIN IMPORT KARNA
# ------------------------------------------------------------

# Sabse pehle Question aur Choice models import karo.
#
# Usually polls/tutorial project mein:
#
from polls.models import Question, Choice

# Ab Question aur Choice Python classes ki tarah available hain.
#
# Question = database table ke ek record ko represent karta hai.
# Choice   = database table ke ek record ko represent karta hai.
#
# Django model basically Python class hoti hai jo database
# table ke saath interact karti hai.


# ------------------------------------------------------------
# 3. DATABASE MEIN EXISTING QUESTIONS DEKHNA
# ------------------------------------------------------------

# Question.objects.all()
#
# objects = Django ka default Manager
# all()    = database se saare Question objects laata hai.
#
# Example:

Question.objects.all()

# Agar database empty hai:
#
# <QuerySet []>
#
# QuerySet = database se aaye objects ka collection.
#
# Agar ek Question hai:
#
# <QuerySet [<Question: Question object (1)>]>
#
# Yahan "1" usually primary key (id) hai.


# ------------------------------------------------------------
# 4. NAYA QUESTION CREATE KARNA
# ------------------------------------------------------------

# Django timezone support use kar raha ho to:
#
from django.utils import timezone

# timezone.now() current date/time deta hai aur timezone
# information ke saath datetime object deta hai.

q = Question(
    question_text="What's new?",
    pub_date=timezone.now()
)

# IMPORTANT:
#
# Upar wale code se Python object create hua hai,
# lekin database mein abhi save nahi hua.
#
# Database mein save karne ke liye save() call karna zaroori hai.

q.save()

# Ab database mein Question insert ho chuka hai.


# ------------------------------------------------------------
# 5. PRIMARY KEY / ID DEKHNA
# ------------------------------------------------------------

q.id

# Output:
#
# 1
#
# Django automatically primary key ke liye "id" field
# create kar deta hai agar humne khud primary key define
# nahi ki hai.


# ------------------------------------------------------------
# 6. MODEL FIELDS KO PYTHON ATTRIBUTES KI TARAH ACCESS KARNA
# ------------------------------------------------------------

q.question_text

# Output:
#
# "What's new?"

q.pub_date

# Output kuch is tarah ho sakta hai:
#
# datetime.datetime(..., tzinfo=datetime.UTC)
#
# Matlab model ke fields ko normal Python attributes ki
# tarah access kar sakte hain.


# ------------------------------------------------------------
# 7. EXISTING OBJECT KO UPDATE KARNA
# ------------------------------------------------------------

# Pehle attribute change karo:

q.question_text = "What's up?"

# Change sirf Python object mein hua hai.
#
# Database mein update karne ke liye dobara save() karo:

q.save()

# Ab database mein question_text bhi update ho gaya.


# ------------------------------------------------------------
# 8. SAARE QUESTIONS DUBARA DEKHNA
# ------------------------------------------------------------

Question.objects.all()

# Ab output kuch aisa ho sakta hai:
#
# <QuerySet [<Question: Question object (1)>]>
#
# Lekin:
#
# "Question object (1)"
#
# user-friendly nahi hai.
#
# Is problem ko __str__() method se solve karenge.


# ============================================================
# 9. __str__() METHOD
# ============================================================

# polls/models.py mein Question model ke andar:

class Question(models.Model):

    # Example fields:
    #
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


# Iska benefit:
#
# Pehle:
#
# <Question: Question object (1)>
#
# Baad mein:
#
# <Question: What's up?>
#
# __str__() Python ko batata hai ki object ko string ke form
# mein represent karte waqt kya text dikhana hai.


# ------------------------------------------------------------
# 10. CHOICE MODEL MEIN BHI __str__()
# ------------------------------------------------------------

class Choice(models.Model):

    # Example:
    #
    # question = models.ForeignKey(
    #     Question,
    #     on_delete=models.CASCADE
    # )
    #
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Ab Choice bhi readable form mein show hoga:
#
# <Choice: Not much>
#
# instead of:
#
# <Choice: Choice object (1)>


# ------------------------------------------------------------
# 11. __str__() IMPORTANT KYUN HAI?
# ------------------------------------------------------------

# __str__() sirf shell ke liye useful nahi hai.
#
# Django Admin bhi model objects ko represent karne ke liye
# __str__() ka use karta hai.
#
# Isliye models mein meaningful __str__() method likhna
# generally good practice hai.


# ============================================================
# 12. CUSTOM MODEL METHOD
# ============================================================

# Ab Question model mein ek custom method banate hain:
#
# was_published_recently()
#
# Iska purpose check karna hai ki Question pichhle 1 din
# ke andar publish hua hai ya nahi.


# Required imports:

import datetime

from django.utils import timezone


class Question(models.Model):

    # ...

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Explanation:
#
# datetime.timedelta(days=1)
#
# = 1 din ka time period.
#
# timezone.now()
#
# = current date/time.
#
# timezone.now() - datetime.timedelta(days=1)
#
# = 24 hours pehle ka time.
#
# Agar:
#
# self.pub_date >= 24_hours_ago
#
# hai, to Question recently published maana jayega.
#
# Method True ya False return karega.


# ------------------------------------------------------------
# 13. CUSTOM METHOD KO CALL KARNA
# ------------------------------------------------------------

q = Question.objects.get(pk=1)

q.was_published_recently()

# Output:
#
# True
#
# Agar Question pichhle 24 hours mein publish hua hai.


# ============================================================
# 14. FILTER() - DATABASE SE SPECIFIC OBJECTS
# ============================================================

# Django ka database API keyword arguments ke through
# powerful filtering provide karta hai.


# ID ke basis par filter:

Question.objects.filter(id=1)

# Equivalent idea:
#
# "Mujhe woh Question objects do jinka id = 1 hai."


# ------------------------------------------------------------
# 15. startswith LOOKUP
# ------------------------------------------------------------

Question.objects.filter(
    question_text__startswith="What"
)

# "__" (double underscore) Django mein lookup operation
# specify karne ke liye use hota hai.
#
# question_text__startswith="What"
#
# Matlab:
#
# question_text "What" se start hona chahiye.
#
# Example:
#
# "What's up?"
#
# match karega.


# ============================================================
# 16. CURRENT YEAR NIKALNA
# ============================================================

from django.utils import timezone

current_year = timezone.now().year

# timezone.now() -> current datetime
# .year          -> us datetime ka year


# ------------------------------------------------------------
# 17. DATE FIELD PAR LOOKUP
# ------------------------------------------------------------

Question.objects.get(
    pub_date__year=current_year
)

# Meaning:
#
# Aisa Question do jiska pub_date ka year current_year ke
# equal ho.
#
# "__year" Django ka field lookup hai.


# ============================================================
# 18. get() AUR EXCEPTION
# ============================================================

Question.objects.get(id=2)

# Agar id=2 exist nahi karta:
#
# DoesNotExist exception raise hogi.
#
# Example:
#
# Question matching query does not exist.


# IMPORTANT DIFFERENCE:
#
# filter() -> QuerySet return karta hai
#
# get()    -> ek single object return karne ki expectation hoti hai
#
# get() tab useful hai jab hume pata ho ki exactly ek object
# milna chahiye.


# ============================================================
# 19. PRIMARY KEY KE LIYE pk
# ============================================================

Question.objects.get(id=1)

# Aur:
#
Question.objects.get(pk=1)

# Dono ka result same hai.
#
# pk = primary key
#
# Django primary key lookup ke liye "pk" shortcut provide karta hai.


# ============================================================
# 20. QUESTION KO VARIABLE MEIN STORE KARNA
# ============================================================

q = Question.objects.get(pk=1)

# Ab q ke andar Question object hai.
#
# Example:
#
# q.question_text
# q.pub_date
# q.id
# q.was_published_recently()


# ============================================================
# 21. FOREIGN KEY RELATIONSHIP
# ============================================================

# Question aur Choice ke beech relationship hai.
#
# Ek Question ke multiple Choices ho sakte hain.
#
# Example:
#
# Question:
# "What's your favorite programming language?"
#
# Choices:
# - Python
# - JavaScript
# - Java
#
# Choice model mein ForeignKey Question ko point karta hai.


# ============================================================
# 22. choice_set
# ============================================================

q = Question.objects.get(pk=1)

q.choice_set.all()

# Agar abhi koi Choice nahi hai:
#
# <QuerySet []>
#
# Django automatically reverse relationship ke liye
# "choice_set" provide karta hai.
#
# choice_set:
#
# Question -> us Question se related Choices


# ============================================================
# 23. CHOICE CREATE KARNA
# ============================================================

q.choice_set.create(
    choice_text="Not much",
    votes=0
)

# Ye ek saath multiple kaam karta hai:
#
# 1. New Choice object create karta hai.
# 2. Us Choice ko q Question ke saath associate karta hai.
# 3. Database mein INSERT karta hai.
# 4. New Choice object return karta hai.
#
# Output:
#
# <Choice: Not much>


# More choices:

q.choice_set.create(
    choice_text="The sky",
    votes=0
)

q.choice_set.create(
    choice_text="Just hacking again",
    votes=0
)


# ============================================================
# 24. CHOICE SE RELATED QUESTION ACCESS KARNA
# ============================================================

c = q.choice_set.create(
    choice_text="Python",
    votes=0
)

c.question

# Output:
#
# <Question: What's up?>
#
# Matlab Choice ke paas "question" attribute hai.
#
# Choice -> Question


# ============================================================
# 25. QUESTION SE CHOICES ACCESS KARNA
# ============================================================

q.choice_set.all()

# Output:
#
# <QuerySet [
#     <Choice: Not much>,
#     <Choice: The sky>,
#     <Choice: Just hacking again>
# ]>
#
# Matlab:
#
# Question -> Choices


# ============================================================
# 26. COUNT()
# ============================================================

q.choice_set.count()

# Output:
#
# 3
#
# count() related objects ki total quantity batata hai.


# ============================================================
# 27. RELATIONSHIPS KE THROUGH FILTERING
# ============================================================

# Django relationships ko follow karne ke liye
# double underscore "__" use karta hai.


Choice.objects.filter(
    question__pub_date__year=current_year
)

# Iska breakdown:
#
# Choice
#   |
#   +-- question
#          |
#          +-- pub_date
#                  |
#                  +-- year
#
#
# Meaning:
#
# "Un Choices ko find karo jinke related Question ka
# pub_date current year mein hai."


# Django relationships ko multiple levels tak follow kar sakta hai.
#
# Example concept:
#
# object__relation__field__lookup
#
# Double underscore hierarchy ko separate karta hai.


# ============================================================
# 28. DELETE()
# ============================================================

# Pehle desired Choice find karo:

c = q.choice_set.filter(
    choice_text__startswith="Just hacking"
)

# Ab delete:

c.delete()

# delete() database se matching objects remove kar deta hai.


# ============================================================
# 29. IMPORTANT DJANGO QUERYSET METHODS
# ============================================================

# all()
#
# Saare objects:

Question.objects.all()


# filter()
#
# Multiple matching objects:

Question.objects.filter(
    question_text__startswith="What"
)


# get()
#
# Ek specific object:

Question.objects.get(pk=1)


# create()
#
# Object create + database mein save:

q.choice_set.create(
    choice_text="Python",
    votes=0
)


# count()
#
# Objects ki quantity:

q.choice_set.count()


# delete()
#
# Objects remove:

q.choice_set.filter(
    choice_text__startswith="Python"
).delete()


# ============================================================
# 30. IMPORTANT LOOKUP EXAMPLES
# ============================================================

# Exact match:
#
Question.objects.filter(id=1)


# Starts with:
#
Question.objects.filter(
    question_text__startswith="What"
)


# Year match:
#
Question.objects.filter(
    pub_date__year=2026
)


# Related model field:
#
Choice.objects.filter(
    question__pub_date__year=2026
)


# Relationship ko "__" se separate kiya jata hai.


# ============================================================
# 31. QUICK MENTAL MODEL
# ============================================================

# Django ORM ko samajhne ka simple formula:
#
# MODEL
#   ↓
# OBJECTS
#   ↓
# QUERYSET
#   ↓
# DATABASE
#
#
# Example:
#
# Question.objects.all()
#
# Question
#    ↓
# objects
#    ↓
# all()
#    ↓
# QuerySet
#    ↓
# Database


# ============================================================
# 32. CRUD CONCEPT
# ============================================================

# Django ORM ke through hum CRUD operations kar sakte hain.
#
# C = Create
# R = Read
# U = Update
# D = Delete


# CREATE:
#
# q = Question(
#     question_text="What's new?",
#     pub_date=timezone.now()
# )
# q.save()


# READ:
#
Question.objects.all()
#
Question.objects.get(pk=1)


# UPDATE:
#
# q.question_text = "What's up?"
# q.save()


# DELETE:
#
q.delete()


# ============================================================
# 33. FINAL SUMMARY
# ============================================================

# Is Django API section se important concepts:
#
# 1. python manage.py shell
#    -> Django project ke context mein Python shell.
#
# 2. Question.objects
#    -> Question model ka database manager.
#
# 3. all()
#    -> Saare objects.
#
# 4. filter()
#    -> Conditions ke basis par objects.
#
# 5. get()
#    -> Specific single object.
#
# 6. save()
#    -> Object ko database mein save/update karta hai.
#
# 7. create()
#    -> Object create karke database mein save karta hai.
#
# 8. delete()
#    -> Database objects delete karta hai.
#
# 9. count()
#    -> Matching objects ki count.
#
# 10. __str__()
#     -> Object ko readable representation deta hai.
#
# 11. Custom methods
#     -> Model ke andar apna business logic likh sakte hain.
#
# 12. ForeignKey
#     -> Models ke beech relationship banata hai.
#
# 13. choice_set
#     -> Related Choice objects ko Question se access karta hai.
#
# 14. "__"
#     -> Django field lookups aur relationships ko navigate
#        karne ke liye use hota hai.
#
#
# Example:
#
# Choice.objects.filter(
#     question__pub_date__year=current_year
# )
#
# Iska matlab:
#
# Choice
#   -> related Question
#       -> pub_date
#           -> year
#               -> current_year
#
#
# Ye hi Django ORM ki sabse powerful cheezon mein se ek hai.
# ============================================================