from django.contrib import admin

from .models import Education, Experience, Resume

class EducationAdmin(admin.ModelAdmin):
    list_display= ('institution_name', 'location', 'degree', 'major', 'gpa')


class ExperienceAdmin(admin.ModelAdmin):
    list_display= ('company', 'title', 'location', 'start_date', 'end_date', 'description')

class ResumeAdmin(admin.ModelAdmin):
     pass

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
