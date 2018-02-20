# Week Lab 4 Django
Andrea Murphy
Project Log: /django/week4

Subject: Python and Django
Purpose: Become familiar with foreign key relationships and unit testing
Description: Update the database to include a foreign key relationship, explore how to retrieve data that is related to another object via a foreign key relationship, add methods to our models, and create automated unit tests.
# Starting point:
 The project is the codebase you have in
            ~/workspace/django/

Make a copy of
    ~/workspace/django/week3 to ~/workspace/django/week4
with
    $ cp -r week3 week4             #You must be in ~/workspace/Django

Use
$ git status                        #to confirm that all the new directories


~/workspace/django/week4            #are untracked

Use
 git add --all and git commit -m 'start week4 Django project'
                                    #to document your new Django project setup

# Details:
- App: "resume"
# Models:
    model.py
    Create a new model named "Resume"
    class Resume(models.Model):
    """
    Model (DB layer) for "resume" app
    """
    First_name = models.CharField(max_length=40, null=False, blank=True)
    Last_name = models.CharField(max_length=40, null=False, blank=True

# Experience Model:
    Add new Foreign Key
class Experience(models.Model):
    """
    Model (DB layer) for "resume" app that hold Experience records
    ForeignKey: Resume
    """
    parent_resume = models.ForeignKey(Resume,on_delete=models.CASCADE,
    default =1)

# Education Model
    Add new Foreign Key

class Education(models.Model):
   """
    Model (DB layer) for "resume" app that hold Education records
    ForeignKey: Resume
         """
      parent_resume = models.ForeignKey(Resume,
      on_delete=models.CASCADE, default =1)

#Django Shell
launch the shell using
    $ python manage.py shell
    (805-env) Andreas-MacBook-Pro:week3 $ python3 manage.py shell

Import your models from command line-
>>> from resume.models import Resume
>>> new_resume = Resume(First_name='Andrea', Last_name='Murphy')
>>> new_resume.save()

>>> Resume.objects.all()
<QuerySet [<Resume: Resume object (1)>]>
>>> Resume.objects.first()
<Resume: Resume object (1)>


# RelatedManager

#To view the reverse side of a foreign key relationship (from the parent, see the children)
    <name of the child model>_set
    from resume.models import Resume
    new_resume.experience_set.all()
<QuerySet [<Experience: Experience object (9)>, <Experience: Experience object (10)>, <Experience: Experience object (11)>, <Experience: Experience object (12)>]>

        #To get the education objects that are related a resume
>>> new_resume.education_set.all()
<QuerySet [<Education: Education object (7)>, <Education: Education object (8)>]>

# Model.Methods
**models.py**

    def get_full_name(self):
        """
        Model.methods
        Returns the persons full name
        """
        return "{} {}".format(self.First_name, self.Last_name)


>>> from resume.models import Resume
>>> full_name = Resume.get_full_name(Resume.objects.first())
>>> full_name
'Andrea Murphy'

    def get_last_name_first_name(self):
        """
        Model.methods
        Returns the persons full name, Last name first
        """
        return "{} {}".format(self.Last_name, self.First_name)

>>> from resume.models import Resume
>>> last_name = Resume.get_last_name_first_name(Resume.objects.first())
>>> last_name
'Murphy Andrea'

# VIEWS
The data is all handled via a resume object
Get the first resume in the database
From that resume, get the related experience and education sets
Passes a single object to the template via the context. The object should be a single resume.

**views.py**
    def index(request):
        """
        Renders the Resume app home template
        Context: Education in query set
        Returns: 'resume/home.html'
        """
        resume = Resume.objects.first()
        context = { 'resume':resume }
    return render(request, 'resume/home.html', context)



# TEMPLATES
Using a resume object and it's class methods
**/resume/home.htmltext**

{% for experience in resume.get_experience %}
       <li>{{experience.company}}</li>
       <li>{{experience.title}}</li>
       <li>{{experience.location}}</li>
       <li>{{experience.start_date}}</li>
       <li>{{experience.end_date}}</li>
       <li>{{experience.description}}</li>
            {% endfor %}
# TESTS
**test.py**
        def setUp(self):
                """
                Setup is ran before every test case
                For each Model create objects for test database
               """
        def each_method_being_testes ():

