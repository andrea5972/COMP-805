from django.db import models
from django.forms import ModelForm

from django.db import models

class Resume(models.Model):
    """
    Model (DB layer) for "resume" app
    """
    First_name = models.CharField(max_length=40, null=False, blank=True)
    Last_name = models.CharField(max_length=40, null=False, blank=True)


class Experience(models.Model):
    """
    Model (DB layer) for "resume" app that hold Experience records
    ForeignKey: Resume
    """
    parent_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default =1)
    company = models.CharField(max_length=40, null=False, blank=True)
    title = models.CharField(max_length=40, null=False, blank=True)
    location = models.CharField(max_length=40, null=False, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()



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


