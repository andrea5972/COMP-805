from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader


from .models import Education, Experience

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





