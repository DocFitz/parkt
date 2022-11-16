from django.contrib import admin
from .models import Course, Hole 
# Register your models here.
class HoleInLine(admin.StackedInline):
    model = Hole
    

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields':['name','description']})
    ] 
    inlines = [HoleInLine]



#split admin form into formsets https://docs.djangoproject.com/en/4.1/intro/tutorial07/
admin.site.register(Course, CourseAdmin)