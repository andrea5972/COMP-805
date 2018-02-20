from django.db import models
from django.forms import ModelForm

class Resume(models.Model):
    """
    Model (DB layer) for "resume" app
    Parent Key: id
    """
    First_name = models.CharField(max_length=40, null=False, blank=True)
    Last_name = models.CharField(max_length=40, null=False, blank=True)


    def get_full_name(self):
        """
        Model.methods
        Returns the persons full name
        """
        return "{} {}".format(self.First_name, self.Last_name)


    def get_last_name_first_name(self):
        """
        Model.methods
        Returns the persons full name, Last name first
        """
        return "{} {}".format(self.Last_name, self.First_name)


    def get_experience(self):
        """
        Model.methods
        Returns the foreign key related to "Experience" objects
        """
        return self.experience_set.all()


    def get_education(self):
        """
        Model.methods
        Returns the foreign key related to "Education" objects
        """
        return  self.education_set.all()



class Experience(models.Model):
    """
    Model (DB layer) for "resume" app that hold Experience records
    ForeignKey: Resume
    """
    parent_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default =1)
    company = models.CharField(max_length=40, null=False, blank=True)
    title = models.CharField(max_length=40, null=False, blank=True)
    location = models.CharField(max_length=40, null=False, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null =True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    """
    Model (DB layer) for "resume" app that hold Education records
    ForeignKey: Resume
    """
    parent_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default =1)
    institution_name = models.CharField(max_length=40, null=False, blank=True)
    location = models.CharField(max_length=40 , null=False, blank=True)
    degree = models.CharField(max_length=40, null=False, blank=True)
    major = models.CharField(max_length=40, null=False, blank=True)
    gpa = models.FloatField(max_length=40, null=False, blank=True)

    def __str__(self):
        return self.institution_name
