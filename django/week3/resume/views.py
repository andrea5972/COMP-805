from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.template import loader


from django.forms import modelformset_factory
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

def manage_education(request):
    """
    """
    EducationFormSet = modelformset_factory(Education, fields=('institution_name', 'location', 'degree', 'major', 'gpa'))
    if request.method == 'POST':
        formset = Education.FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = EducationFormSet()
    return render(request,  'resume/education.html', {'formset': formset})

def get_field(self):
    """
    """
    new_education = Education.objects.get(structidx__exact=id).get_fields()
    return render_to_response('resume/home.html', { 'new_education' : new_education}, context_instance = RequestContext(request))
