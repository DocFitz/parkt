from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='scorecard'),
    path('home', views.home, name='home'),
    path('create_course', views.create_course, name='create_course'),
    path('edit_course/<uuid:pk>', views.edit_course, name='edit_course'),
    path('view_course', views.view_course, name='view_course' ),
    path('details/<uuid:pk>', views.course_detail, name='details'),
    path('template', views.template, name='template')
]
