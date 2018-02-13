from django.db import models
from django.forms import ModelForm

class Education(models.Model):
    """
    Model (DB layer) for Andrea Murphy's education records

    """
    institution_name = models.CharField(max_length=40, null=False, blank=True)
    location = models.CharField(max_length=40 , null=False, blank=True)
    degree = models.CharField(max_length=40, null=False, blank=True)
    major = models.CharField(max_length=40, null=False, blank=True)
    gpa = models.FloatField(max_length=40, null=False, blank=True)

    def __str__(self):
        """
        Returns fields attached to Education models.
        """
        if not hasattr(self, 'model'):
            return super().__str__()
        model = self.Education
        app = Education._meta.app_label
        return '%s.%s.%s' % (resume, Education._meta.object_name, self.name)


class EducationForm(ModelForm):
    class Meta:
       model = Education
       fields = ['institution_name', 'location', 'degree', 'major', 'gpa']


class Experience(models.Model):
    """
    Model (DB layer) for Andrea Murphy professional work experience
    """
    company = models.CharField(max_length=40, null=False, blank=True)
    title = models.CharField(max_length=40, null=False, blank=True)
    location = models.CharField(max_length=40, null=False, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        """
        Returns fields attached to Experience models.
        """
        if not hasattr(self, 'model'):
            return super().__str__()
        model = self.Experience
        app = Experience._meta.app_label
        return '%s.%s.%s' % (resume, Experience._meta.object_name, self.name)

class ExperienceForm(ModelForm):
    class Meta:
       model = Experience
       fields = ['company', 'title', 'location', 'start_date', 'end_date', 'description']


