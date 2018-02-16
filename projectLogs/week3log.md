**Lab 3 Django**

Andrea Murphy

Project Log for: django/week3

**Subject** : Python and Django

**Purpose** : Become familiar with Django apps, models, the admin panel, and query sets

**Description** : In this lab we will add dynamic data to our resume page. Using Django models, create a new app, called &quot;resume&quot;, link the **ROOT\_URLCONF** to the **apps.urls** , create two models, add data to our database, and display the data to the user using a template.



**Starting point:**

 The project is the codebase you have in

**~/workspace/django/week2**

Make a copy of

  **~/workspace/django/week2** to **~/workspace/django/week3**

with

**$ cp -r week2 week3**                      #You must be in ~/workspace/Django

Use

**$ git**** status                                          ** #to confirm that all the new directories



        **~/workspace/django/week3**                 #are untracked

Use

  **git add --all** and **git commit -m &#39;start week3 Django project&#39;**

#to document your new Django project setup

**Details**

1. App: &quot;resume&quot;
  - Create a new app that is named &quot;resume&quot;
  - add &quot;resume&quot; to your installed\_apps in **settings.py**

INSTALLED\_APPS = [

    &#39;django.contrib.admin&#39;,

    &#39;django.contrib.auth&#39;,

    &#39;django.contrib.contenttypes&#39;,

    &#39;django.contrib.sessions&#39;,

    &#39;django.contrib.messages&#39;,

    &#39;django.contrib.staticfiles&#39;,

    &#39;resume&#39;,

]

1.  Create py
  - Experience Model

class Experience(models.Model):

    &quot;&quot;&quot;

    Model (DB layer) for Andrea Murphy professional work experience

    &quot;&quot;&quot;

    company = models.CharField(max\_length=40)

    title = models.CharField(max\_length=40)

    location = models.CharField(max\_length=40)

    start\_date = models.DateField()

    end\_date = models.DateField()

    description = models.TextField()



    def \_\_str\_\_(self):

            return self.company

-
  - Education Model

class Education(models.Model):

    &quot;&quot;&quot;

    Model (DB layer) for Andrea Murphy&#39;s education records

    &quot;&quot;&quot;



    institution\_name = models.CharField(max\_length=40)

    location = models.CharField(max\_length=40)

    degree = models.CharField(max\_length=40)

    major = models.CharField(max\_length=40)

    gpa = models.FloatField(max\_length=40)

        def \_\_str\_\_(self):

            return self.title

- Django Shell
  - Launch the shell using-

(805-env) Andreas-MacBook-Pro:week3 $ python3 manage.py shell

-
  - Import your models from command line-

        &gt;&gt;&gt;from resume.models import Education

new\_education = Education(institution\_name=&quot;UNH&quot;, location=&quot;Manchester, NH&quot;, degree=&quot;Masters of Science &quot;, major=&quot;IT&quot;, gpa=3.8, name=&quot;Education&quot;)

&gt;&gt;&gt;new\_education.save()        #must save at each new entry

new\_education = Education(institution\_name=&quot;VCU&quot;, location= &quot;Richmond,VA&quot;, degree= &quot;Bachelor of Science&quot;,major=&quot;Business Marketing&quot;, gpa=3.5, name=&quot;Education&quot;)

&gt;&gt;&gt;new\_education.save()

&gt;&gt;&gt;from resume.models import Experience

new\_experience = Experience(company= &quot;Three Owl Design&quot;, title= &quot;Founder and Principal Operator&quot;, location=&quot;New Boston, NH&quot;, start\_date= &#39;2015-05-01&#39;, end\_date= &#39;2018-02-01&#39;, description=&quot; Communications and Cross-functional Virtual Marketing Manager, Web and Graphic Designer&quot;, name = &quot;Experience&quot;)

&gt;&gt;&gt;new\_experience.save()

new\_experience = Experience(company= &quot;Canvas on the Road&quot;, title= &quot;Owner and Principal Art Teacher&quot;, location=&quot;New Hampshire&quot;, start\_date= &#39;2016-11-01&#39;, end\_date= &#39;2018-02-01&#39;, description=&quot;Operations management and, marketing graphic and web design, teach varies types of art classes&quot;, name = &quot;Experience&quot;)

&gt;&gt;&gt;new\_experience.save()

new\_experience = Experience(company= &quot;Dawkins Productions&quot;, title= &quot;Marketing Director&quot;, location=&quot;Richmond, VA&quot;, start\_date= &#39;2014-04-01&#39;, end\_date= &#39;2015-05-01&#39;, description=&quot;Operations management, social marketing planning and execution, graphic and web design, intern program manager&quot;, name = &quot;Experience&quot;)



&gt;&gt;&gt;new\_experience.save()



new\_experience = Experience(company= &quot;Perfect Harmony&quot;, title= &quot;Owner and Principal Operator&quot;, location=&quot;Richmond, VA&quot;, start\_date= &#39;2008-05-01&#39;, end\_date= &#39;2015-09-01&#39;, description=&quot;Operations management and, marketing graphic and web design, therapeutic massages with ROM, and chiropractic care&quot;, name = &quot;Experience&quot;)

&gt;&gt;&gt;new\_experience.save()



-
  - Confirm the objects were saved by using query sets

&gt;&gt;&gt;education\_queryset = Education.objects.all()



- Admin Panel
  - Register these models with the admin panel in ( **resume/admin.py** module)

from django.contrib import admin

from django.contrib import admin

from .models import Education, Experience

class EducationAdmin(admin.ModelAdmin):

pass

class ExperienceAdmin(admin.ModelAdmin):

pass



admin.site.register(Education, EducationAdmin)

admin.site.register(Experience, ExperienceAdmin)

-
  - Confirm all your entries were saved by viewing them in the admin panel



- Urls-Views-Templates:

**URLS**

**resume/urls.py**

urlpatterns = [

    path(&#39;&#39;, views.index, name=&#39;index&#39;),

]

**portfolioplus/urls.py**

#Use include( ) function from django.conf.urls in your call to path( )

path(r&#39;resume/&#39;, include(&#39;resume.urls&#39; , namespace = &#39;resume&#39;)),

-
  -
    - Create a new path that will correspond to a new view



**resume/views.py**

def index(request):

    &quot;&quot;&quot;

    Renders the Resume app home template

    Context: Education in query set

    Returns: &#39;resume/home.html&#39;

    &quot;&quot;&quot;

    qs1 = Education.objects.all()

    qs2 = Experience.objects.all()

    context = {&#39;new\_education&#39;:qs1, &#39;new\_experience&#39;: qs2 }

    return render(request, &#39;resume/home.html&#39;, context)









**Template:**

**resume/home.html**

{% extends &#39;base.html&#39; %}

{% block content %}

  &lt;div class=&#39;resume-banner&#39;&gt;

            &lt;h1&gt;Andrea Murphy&lt;/h1&gt;

            &lt;hr&gt;

  &lt;div class=&#39;resume-content&#39;&gt;

{% if new\_education %}

  &lt;ul&gt;

    {% for Education in new\_education %}

      &lt;li&gt;{{ Education.institution\_name }}&lt;/a&gt;

      &lt;li&gt;{{ Education.location }}&lt;/li&gt;

      &lt;li&gt;{{ Education.degree }}&lt;/li&gt;

      &lt;li&gt;{{ Education.major }}&lt;/li&gt;

      &lt;li&gt;{{ Education.gpa }}&lt;/li&gt;

    {% endfor %}

  &lt;/ul&gt;

  {% else %}

    &lt;h1&gt;Contact an Admin!&lt;/h1&gt;

  {% endif %}

{% if new\_experience %}

  &lt;ul&gt;

    {% for Experience in new\_experience %}

      &lt;li&gt;{{Experience.company}}&lt;/li&gt;

      &lt;li&gt;{{Experience.title}}&lt;/li&gt;

      &lt;li&gt;{{Experience.location}}&lt;/li&gt;

      &lt;li&gt;{{Experience.start\_date}}&lt;/li&gt;

      &lt;li&gt;{{Experience.end\_date}}&lt;/li&gt;

      &lt;li&gt;{{Experience.description}}&lt;/li&gt;

    {% endfor %}

  &lt;/ul&gt;

  {% else %}

    &lt;h1&gt;Contact an Admin!&lt;/h1&gt;

    {% endif %}

  {% endblock %}

  &lt;/div&gt;

&lt;/div&gt;
