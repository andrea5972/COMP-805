from django.shortcuts import render
from django.template import loader

from .models import Resume

def index(request):
    """
    Renders the Resume app home template
    Context: Education in query set
    Returns: 'resume/home.html'
    """

    resume = Resume.objects.first()

    context = { 'resume':resume }
    return render(request, 'resume/home.html', context)

