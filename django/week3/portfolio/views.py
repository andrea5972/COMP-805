from django.shortcuts import render

def home(request):
    """
    Renders the home page for the web application portfolio "Andrea Murphy"
    Retuns: the home.html page
    """
    context = {}
    return render(request, 'home.html', context)

def portfolio(request):
    """
    Renders my Portfolio static page template
    Retuns: the portfolio.html page
    """
    context = {}
    return render(request, 'portfolio.html', context)


def contact(request):
    """
    Renders my Contact static page template
    Retuns: the contact.html page
    """
    context = {}
    return render(request, 'contact.html', context)
