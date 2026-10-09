```python
# ============================================================
# DJANGO VIEWS AUR URLCONF - EASY HINGLISH EXPLANATION
# ============================================================

# BHAI, VIEW KYA HOTA HAI?
#
# Django mein View ek Python function hota hai jo user ki request
# receive karta hai aur uske according response return karta hai.
#
# Example:
# Blog homepage par latest blogs dikhana.
# Question page par question dikhana.
# Results page par voting ke results dikhana.
# Vote view ke through user ka vote handle karna.
#
# Har view ka ek specific kaam ho sakta hai.
# View HTML page, simple text, JSON, PDF ya koi aur response
# return kar sakta hai.
#
# DJANGO MEIN URLCONF KYA HOTA HAI?
#
# URLconf ka kaam URL ko sahi view function se connect karna hai.
# Matlab user kaunsi URL open karta hai, uske according Django
# decide karta hai ki kaunsa Python function run hoga.
#
# Example:
# /polls/         -> index view
# /polls/5/       -> detail view
# /polls/5/results/ -> results view
# /polls/5/vote/ -> vote view
#
# Django sabse pehle project ke urls.py ko check karta hai.
# ROOT_URLCONF setting Django ko batati hai ki project ka
# main URL configuration module kaunsa hai.
#
# Agar project ke urls.py mein "polls/" ka pattern milta hai,
# toh Django "polls/" ko hata kar remaining URL ko polls/urls.py
# mein check karta hai.
#
# Example:
# /polls/34/
#
# Project URLconf "polls/" ko match karta hai.
# Remaining URL "34/" polls/urls.py ko milta hai.
# Wahan <int:question_id>/ match hota hai.
# Isliye detail(request, question_id=34) call hota hai.
#
# <int:question_id> KA MATLAB:
#
# int ek URL converter hai jo integer value match karta hai.
# question_id us value ka naam hai jo view ko pass hota hai.
#
# Example:
# /polls/34/ -> question_id = 34
#
# ============================================================
# AB PRACTICAL CODE SAMAJHTE HAIN
# ============================================================

# Django se HttpResponse import kar rahe hain.
# Iska use browser ko response bhejne ke liye hota hai.
from django.http import HttpResponse

# models.py se Question model import kar rahe hain.
# Is model ki help se database mein stored questions access honge.
from .models import Question


# ============================================================
# 1. INDEX VIEW
# ============================================================

# Ye function polls ki homepage ke liye hai.
# Jab user /polls/ open karega, toh URLconf index view ko call karega.
def index(request):

    # Question.objects database ke Question records ko access karta hai.
    #
    # order_by("-pub_date") ka matlab publication date ke according
    # questions ko latest se oldest order mein arrange karna.
    #
    # Minus (-) ka matlab descending order hai.
    #
    # [:5] ka matlab maximum 5 questions lena.
    #
    # Example:
    # Database mein 20 questions hain, toh latest 5 questions milenge.
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # Ab har question ka question_text nikal rahe hain.
    #
    # q ek question object ko represent karta hai.
    # q.question_text us question ka text deta hai.
    #
    # List comprehension:
    # [q.question_text for q in latest_question_list]
    #
    # Iska matlab har question par loop chalao aur uska text lo.
    #
    # ", ".join(...) saare question texts ko comma aur space se
    # jod kar ek single string bana deta hai.
    #
    # Example:
    # ["First question", "Second question", "Third question"]
    #
    # Output:
    # "First question, Second question, Third question"
    output = ", ".join(
        [q.question_text for q in latest_question_list]
    )

    # HttpResponse browser ko response bhejta hai.
    # Abhi questions simple text ke form mein dikhaye jayenge,
    # HTML template ke form mein nahi.
    return HttpResponse(output)


# ============================================================
# 2. DETAIL VIEW
# ============================================================

# Ye view kisi particular question ki detail page ke liye hai.
#
# Example URL:
# /polls/34/
#
# Django URL se 34 ko question_id ke roop mein capture karega.
# Phir detail function ko request aur question_id pass karega.
def detail(request, question_id):

    # %s ek placeholder hai.
    # % question_id us placeholder ki jagah actual ID insert karta hai.
    #
    # Agar question_id = 34 hai, toh response hoga:
    # "You're looking at question 34."
    #
    # IMPORTANT:
    # Ye sirf demo message hai.
    # Abhi database se actual question fetch nahi ho raha.
    return HttpResponse("You're looking at question %s." % question_id)


# ============================================================
# 3. RESULTS VIEW
# ============================================================

# Ye view kisi particular question ke results ke liye hai.
#
# Example URL:
# /polls/34/results/
#
# Is URL se question_id = 34 milega.
def results(request, question_id):

    # Ek message string bana rahe hain.
    # %s ki jagah question ki ID insert hogi.
    response = "You're looking at the results of question %s."

    # Question ID ko message mein insert karke browser ko bhej rahe hain.
    #
    # Example output:
    # "You're looking at the results of question 34."
    #
    # IMPORTANT:
    # Abhi actual voting results calculate nahi ho rahe.
    # Ye sirf placeholder response hai.
    return HttpResponse(response % question_id)


# ============================================================
# 4. VOTE VIEW
# ============================================================

# Ye view kisi particular question par vote karne ke action ke liye hai.
#
# Example URL:
# /polls/34/vote/
#
# Is URL se question_id = 34 milega.
def vote(request, question_id):

    # Abhi sirf ek message browser ko return kar rahe hain.
    #
    # Example output:
    # "You're voting on question 34."
    #
    # IMPORTANT:
    # Abhi vote save nahi ho raha.
    # Actual voting ke liye user ki selected choice receive karni hogi,
    # us choice ko validate karna hoga aur database mein vote count
    # update karna hoga.
    return HttpResponse("You're voting on question %s." % question_id)


# ============================================================
# QUICK REVISION - BHAI YE YAAD RAKHNA
# ============================================================

# VIEW:
# Python function jo request process karke response return karta hai.
#
# URLCONF:
# URL patterns ko views se connect karta hai.
#
# request:
# User ki HTTP request ki information rakhta hai.
#
# question_id:
# URL se aane wali question ki ID hai.
#
# HttpResponse:
# Browser ko response bhejta hai.
#
# Question.objects:
# Database ke Question records ko access karta hai.
#
# order_by("-pub_date"):
# Latest questions ko pehle laata hai.
#
# [:5]:
# Sirf pehle 5 records select karta hai.
#
# q.question_text:
# Question ka actual text deta hai.
#
# ", ".join(...):
# Multiple strings ko comma aur space se jodta hai.
#
# FINAL FLOW:
#
# User URL open karta hai
#         |
#         v
# Project urls.py URL match karta hai
#         |
#         v
# polls/urls.py correct view select karta hai
#         |
#         v
# View apna kaam karta hai
#         |
#         v
# HttpResponse browser ko response bhejta hai
#
# NOTE:
# Ye poora code polls/views.py ke liye hai.
# URL patterns alag se polls/urls.py mein define hote hain.
# ============================================================
```
