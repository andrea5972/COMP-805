from django.shortcuts import render

def home(request):
    """
    Renders the home page for the web application portfolio "Andrea Murphy"
    Retuns: the home.html page
    """
    context = {}
    return render(request, 'home.html', context)

    def resume(request):
    """
    Renders my Resume static page template
    Retuns: the resume.html page
    """
    context = {}
    return render(request, 'resume.html', context)

    def portfolio(request):
    """
    Renders my Portfolio static page template
    Retuns: the portfolio.html page
    """
    context = {}
    return render(request, 'portfolio.html', context)
