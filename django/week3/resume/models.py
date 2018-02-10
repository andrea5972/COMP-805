from django.db import models


class Experience(models.Model):
    """
    Model (DB layer) for Andrea Murphy professional work experience
    """
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=40)


    def __str__(self):
            return self.title

class Education(models.Model):
    """
    Model (DB layer) for Andrea Murphy's education records

    """
    institution_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    degree = models.CharField(max_length=40)
    major = models.CharField(max_length=40)
    gpa = models.FloatField(max_length=40)

    def __str__(self):
        return "{} , {}".format(self.front, self.back)
