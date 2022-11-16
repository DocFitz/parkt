from django.forms import ModelForm, inlineformset_factory
from course_keeper.models import Course, Hole

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class HoleCreateForm(ModelForm):
    class Meta:
        model = Hole
        fields = ['hole_number','length','name','par','target','hazard','out_boundary','mando']