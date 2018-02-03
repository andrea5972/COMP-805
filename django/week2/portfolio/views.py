from django.shortcuts import render

def home(request):
    """
    Renders the home page for the web application portfolio "Andrea Murphy"
    Retuns: the home.html page
    """
    context = {}
    return render(request, 'home.html', context)
