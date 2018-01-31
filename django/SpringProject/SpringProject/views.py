from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "Bloom!"
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting, 'weekday_list':days_of_week}
    return render(request, 'home.html', context)
