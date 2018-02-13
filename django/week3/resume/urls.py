from django.urls import path

from . import views

app_name = 'resume'
urlpatterns = [
    path(r'index/', views.index, name='index'),
]
