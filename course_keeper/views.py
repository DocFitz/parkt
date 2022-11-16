from django.shortcuts import render, redirect
from course_keeper.forms import CourseCreateForm, HoleCreateForm
from course_keeper.models import Course, Hole


#play a game, data stored in session info
def scorecard(request):
    
    return render(request, 'scorecard.html', context={})

#create a course
def create_course(request):
    #check to see if the request is a post which means form is filled out
    if request.method == 'POST':
        courseForm = CourseCreateForm(request.POST)
        if courseForm.is_valid():
            print('form is valid')
            #create a new course and save to db
            course = courseForm.save()
            return redirect('edit_course', course.id)
        else:
            error = 'course name is not unique'
            courseForm = CourseCreateForm()
            context={'error_msg':error,'courseForm':courseForm}
            return render(request, 'create_course.html', context)
        
    else:
        courseForm = CourseCreateForm()

    return render(request, 'create_course.html', context={'courseForm':courseForm})

def edit_course(request, pk):

    course = Course.objects.get(id=pk)
    courseForm = CourseCreateForm(instance=course)

    holes = Hole.objects.filter(course_id=pk)
    print('course has ' +str(len(holes)) + 'num of holes')
    holelist = []
    #add one blank hole at the begining
    holeForm = HoleCreateForm()
    holelist.insert(0, holeForm)
    #get the existing holes for the given course
    for hole in holes:
        hole = Hole.objects.get(id=hole.id)
        holeForm = HoleCreateForm(instance=hole)
        holelist.append(holeForm)

    return render(request, 'edit_course.html', context={'courseForm':courseForm,'holelist':holelist})

def delete_hole(request, pk):
    pass



def course_detail(request,pk):
    course = Course.objects.get(id=pk)
    holes = Hole.objects.filter(course_id=pk)
    
    print(course)
    return render(request, 'course_detail.html', context = {'course':course,'holes':holes})

def view_course(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', context={'courses':courses})

#View all options and updates
def home(request):
    return render(request, 'home.html', context={})

#page to view all the html template
def template(request):
    return render(request, 'w3_template.html', context={})
