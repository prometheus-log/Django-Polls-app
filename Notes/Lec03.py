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