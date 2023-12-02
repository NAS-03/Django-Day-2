from django.contrib import admin
from courses.models import Courses
# Register your models here.


class CourseView(admin.ModelAdmin):
    list_display = [
        "id", "course_name",'instructor','course_length']
    

admin.site.register(Courses,CourseView)


