# ============================================================
# DJANGO ADMIN – EASY HINGLISH NOTES
# ============================================================

# Django Admin kya hai?
# ---------------------
# Django Admin ek ready-made interface hai jahan admin/staff:
# - Data add kar sakte hain
# - Existing data edit/change kar sakte hain
# - Data delete kar sakte hain
#
# Simple words:
# Django khud ek Admin Panel bana deta hai.
# Hume admin panel manually design karne ki zarurat nahi hoti.
#
# Example:
# Agar ek News Website hai, to admin:
# - News add karega
# - News edit karega
# - News delete karega
#
# IMPORTANT:
# Django Admin normal website visitors ke liye nahi hota.
# Ye mainly site managers / administrators ke liye hota hai.


# ============================================================
# 1. CREATING AN ADMIN USER
# ============================================================

# Sabse pehle hume ek admin/superuser banana padta hai.
#
# Command:
#
# python manage.py createsuperuser
#
# Is command ke baad Django humse poochega:
#
# Username: admin
# Email: admin@example.com
# Password: ********
#
# Password ko confirmation ke liye dobara enter karna hota hai.
#
# Agar sab sahi raha to message aayega:
#
# Superuser created successfully.
#
# Simple meaning:
# Superuser = Django Admin Panel ka main/admin user.


# ============================================================
# 2. START THE DEVELOPMENT SERVER
# ============================================================

# Admin panel use karne ke liye Django server start karo.
#
# Command:
#
# python manage.py runserver
#
# Server start hone ke baad browser mein open karo:
#
# http://127.0.0.1:8000/admin/
#
# Ye Django Admin ka login page open karega.
#
# Yahan hum apne banaye hue superuser ke:
# - Username
# - Password
# enter karke login karenge.


# ============================================================
# 3. ENTER THE ADMIN SITE
# ============================================================

# Login karne ke baad Django Admin ka main/index page dikhega.
#
# By default Django mein kuch models already available hote hain,
# jaise:
#
# - Users
# - Groups
#
# Ye Django ke authentication system se aate hain.
#
# Authentication ka simple meaning:
# User ko login karna aur uski permissions manage karna.


# ============================================================
# 4. APNI APP KO ADMIN PANEL MEIN ADD KARNA
# ============================================================

# Ab maan lo hamare paas "polls" naam ki app hai.
#
# Usme Question naam ka model hai.
#
# Lekin Question admin panel mein automatically nahi dikhega.
#
# Hume Django ko batana padega:
#
# "Bhai, Question model ko Admin Panel mein dikhao."


# ============================================================
# 5. polls/admin.py FILE
# ============================================================

# polls/admin.py mein ye code likho:


from django.contrib import admin
from .models import Question

admin.site.register(Question)


# Explanation:
#
# from django.contrib import admin
# --------------------------------
# Django ka admin module import kar rahe hain.
#
#
# from .models import Question
# ----------------------------
# Hamare models.py file se Question model import kar rahe hain.
#
# "." ka meaning:
# Current app/package.
#
#
# admin.site.register(Question)
# ----------------------------
# Question model ko Django Admin ke saath register kar rahe hain.
#
# Simple words:
# "Django, Question model ko Admin Panel mein dikha de."


# ============================================================
# 6. AB ADMIN PANEL MEIN KYA DIKHEGA?
# ============================================================

# Server start karo:
#
# python manage.py runserver
#
# Browser:
#
# http://127.0.0.1:8000/admin/
#
# Login karne ke baad ab "Questions" option dikhega.
#
# Uspe click karne par database mein stored
# saare Question objects dikhenge.


# ============================================================
# 7. QUESTION KO EDIT KARNA
# ============================================================

# Agar Question mein koi data already saved hai,
# to admin panel se usko edit kar sakte hain.
#
# Example:
#
# Question:
# "What's up?"
#
# Is question par click karke uska data change kar sakte hain.
#
# Django automatically Question model ke basis par
# editing form create karta hai.


# ============================================================
# 8. DJANGO AUTOMATICALLY FORM BANATA HAI
# ============================================================

# Django Admin ka ek major advantage:
#
# Hume HTML form manually banane ki zarurat nahi hoti.
#
# Django model ke fields ko dekhkar automatically
# appropriate form fields create karta hai.
#
# Example:
#
# models.py:
#
# question_text = CharField(...)
# pub_date = DateTimeField(...)
#
# Django Admin automatically appropriate input fields
# generate karega.


# ============================================================
# 9. FIELD TYPES KE ACCORDING WIDGETS
# ============================================================

# Django model ke different field types ke liye
# appropriate HTML input widgets automatically milte hain.
#
# Example:
#
# CharField
# -> Text input
#
# DateTimeField
# -> Date + Time related input
#
# Isliye hume manually HTML input design nahi karna padta.


# ============================================================
# 10. DATETIMEFIELD KI EXTRA FACILITIES
# ============================================================

# DateTimeField ke liye Django Admin kuch
# useful JavaScript shortcuts deta hai.
#
# Example:
#
# "Today"
# -> Aaj ki date automatically select karne ke liye.
#
# "Now"
# -> Current time automatically select karne ke liye.
#
# Calendar popup bhi available hota hai.
#
# Isse date/time enter karna easy ho jata hai.


# ============================================================
# 11. SAVE OPTIONS
# ============================================================

# Django Admin mein object edit karne ke baad
# neeche different buttons milte hain.


# 1. SAVE
# -------
# Changes save karega aur wapas change-list page par le jayega.


# 2. SAVE AND CONTINUE EDITING
# ----------------------------
# Changes save karega aur same object ki editing page
# par hi rakhega.
#
# Useful jab hume same object ko aur edit karna ho.


# 3. SAVE AND ADD ANOTHER
# -----------------------
# Current object save karega aur ek new blank form open karega.
#
# Useful jab multiple objects ek ke baad ek add karne ho.


# 4. DELETE
# ---------
# Current object ko delete karne ka option deta hai.
#
# Delete karne se pehle confirmation page aata hai.


# ============================================================
# 12. HISTORY
# ============================================================

# Django Admin mein "History" option bhi hota hai.
#
# History page par hum dekh sakte hain:
#
# - Object mein kya changes hue
# - Change kab hua
# - Kis user/admin ne change kiya
#
# Simple words:
# History = Object ke changes ka record.


# ============================================================
# 13. TIME_ZONE
# ============================================================

# Agar Admin Panel mein "Date published"
# ka time galat show ho raha hai,
# to TIME_ZONE setting check karni chahiye.
#
# settings.py mein:
#
# TIME_ZONE = "Asia/Kolkata"
#
# India ke liye generally Asia/Kolkata use kiya jata hai.
#
# Wrong TIME_ZONE hone par date/time incorrect
# display ho sakta hai.


# ============================================================
# COMPLETE FLOW – EXAM KE LIYE IMPORTANT
# ============================================================

# Django Admin ka basic flow:
#
# 1. Superuser create karo
#
#    python manage.py createsuperuser
#
# 2. Server start karo
#
#    python manage.py runserver
#
# 3. Browser mein Admin open karo
#
#    http://127.0.0.1:8000/admin/
#
# 4. Superuser se login karo.
#
# 5. Model ko admin.py mein register karo.
#
#    admin.site.register(Question)
#
# 6. Ab Question Admin Panel mein show hoga.
#
# 7. Admin se Question:
#    - Add
#    - Edit
#    - Delete
#    kar sakta hai.
#
# 8. Django automatically forms aur suitable widgets provide karta hai.


# ============================================================
# ONE-LINE SUMMARY
# ============================================================

# Django Admin ek automatic, ready-made admin interface hai
# jiske through authorized users models ke data ko
# easily ADD, EDIT aur DELETE kar sakte hain.
#
# Main command:
#
# python manage.py createsuperuser
#
# Main registration:
#
# admin.site.register(Question)


# ============================================================
# EXAM POINTS – 5 MARKS
# ============================================================

# Django Admin:
#
# 1. Django automatically admin interface provide karta hai.
# 2. Iska use site administrators/staff ke liye hota hai.
# 3. Superuser banane ke liye createsuperuser command use hoti hai.
# 4. Models ko admin.py mein register karke Admin Panel mein show
#    karaya ja sakta hai.
# 5. Admin se data Add, Edit aur Delete kiya ja sakta hai.
# 6. Django model fields ke according forms/widgets automatically
#    generate karta hai.
# 7. History feature changes ka record maintain karta hai.