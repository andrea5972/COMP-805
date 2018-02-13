from django.db import models

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
        String for representing the Model object.
        """
        return self.institution_name, location, degree, major, gpa

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
            return self.company, title, location, start_date, end_date, description



