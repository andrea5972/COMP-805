from django.contrib import admin

from django.contrib import admin
from .models import Education, Experience

class EducationAdmin(admin.ModelAdmin):
    list_display= ('institution_name', 'location', 'degree', 'major', 'gpa')


class ExperienceAdmin(admin.ModelAdmin):
    list_display= ('company', 'title', 'location', 'start_date', 'end_date', 'description')

def push_live(modeladmin, request, queryset):
    queryset.update( )
push_live.short_description = "Mark selected Decks as active"


admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
