# Week 3 Django
Andrea Murphy
Project Log for:
django/week3

**Subject** : Python and Django
**Purpose** : Become familiar with Django apps, models, the admin panel, and query sets

**Description** : In this lab we will add dynamic data to our resume page. Using Django models, create a new app, called 'resume', link the **ROOT\_URLCONF** to the **apps.urls** , create two models, add data to our database, and display the data to the user using a template.

**Starting point:**
The project is the codebase-
**~/workspace/django/week2**
Make a copy of
**~/workspace/django/week2** to **~/workspace/django/week3**
with
**$ cp -r week2 week3**       #You must be in ~/workspace/Django
Use
**$ git status**              #to confirm that all the new directories
Use
 **git add --all** and **git commit -m &#39;start week3 Django project&#39;**
#to document your new Django project setup

# Details:
 App:
  - Create a new app that is named- 'resume'
  - add to your installed apps in **settings.py**

INSTALLED\_APPS = [


        'resume',

]

# Experience Model

class Experience(models.Model):
    """
    Model (DB layer) for Andrea Murphy professional work experience
    """
    company = models.CharField(max\_length=40)

    title = models.CharField(max\_length=40)

    location = models.CharField(max\_length=40)

    start\_date = models.DateField()

    end\_date = models.DateField()

    description = models.TextField()

    def \_\_str\_\_(self):
            return self.title

# Education Model

class Education(models.Model):
    """
    Model (DB layer) for Andrea Murphy&#39;s education records
    """
    institution\_name = models.CharField(max\_length=40)

    location = models.CharField(max\_length=40)

    degree = models.CharField(max\_length=40)

    major = models.CharField(max\_length=40)

    gpa = models.FloatField(max\_length=40)

        def \_\_str\_\_(self):

            return self.title

# Django Shell
  - Launch the shell using-
(805-env) Andreas-MacBook-Pro:week3 $ ***python3 manage.py shell***
Import your models from command line-

from resume.models import Education
new_education = Education(institution_name="UNH", location="Manchester, NH", degree="Masters of Science ", major="IT", gpa=3.8, name="Education")

>>>new_education.save() #must save at each new entry

new_education = Education(institution_name="VCU", location= "Richmond,VA", degree= "Bachelor of Science",major="Business Marketing", gpa=3.5, name="Education")

>>>new_education.save()

>>>from resume.models import Experience

new_experience = Experience(company= "Three Owl Design", title= "Founder and Principal Operator", location="New Boston, NH", start_date= '2015-05-01', end_date= '2018-02-01', description=" Communications and Cross-functional Virtual Marketing Manager, Web and Graphic Designer", name = "Experience")

>>>new_experience.save()

new_experience = Experience(company= "Canvas on the Road", title= "Owner and Principal Art Teacher", location="New Hampshire", start_date= '2016-11-01', end_date= '2018-02-01', description="Operations management and, marketing graphic and web design, teach varies types of art classes", name = "Experience")

>>>new_experience.save()

new_experience = Experience(company= "Dawkins Productions", title= "Marketing Director", location="Richmond, VA", start_date= '2014-04-01', end_date= '2015-05-01', description="Operations management, social marketing planning and execution, graphic and web design, intern program manager", name = "Experience")


>>>new_experience.save()


new_experience = Experience(company= "Perfect Harmony", title= "Owner and Principal Operator", location="Richmond, VA", start_date= '2008-05-01', end_date= '2015-09-01', description="Operations management and, marketing graphic and web design, therapeutic massages with ROM, and chiropractic care", name = "Experience")

>>>new_experience.save()

Confirm the objects were saved by using query sets

>>>education_queryset = Education.objects.all()


# Admin Panel
Register these models with the admin panel in ***resume/admin.py module***
from django.contrib import admin
from django.contrib import admin
from .models import Education, Experience

class EducationAdmin(admin.ModelAdmin):
pass

class ExperienceAdmin(admin.ModelAdmin):
pass

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)

- Confirm all your entries were saved by viewing them in the admin panel


# Urls-Views-Templates:
***URLS***
**resume/urls.py**

urlpatterns = [
    path('', views.index, name='index'),
]

***portfolioplus/urls.py***

#Use include( ) function from django.conf.urls in your call to path( )

***path(r'resume/', include('resume.urls' , namespace = 'resume'))***

# Views

resume/views.py

def index(request):
    """
    Renders the Resume app home template
    Context: Education in query set
    Returns: 'resume/home.html'
    """
    qs1 = Education.objects.all()
    qs2 = Experience.objects.all()

    context = {'new_education':qs1, 'new_experience': qs2 }
    return render(request, 'resume/home.html', context)

