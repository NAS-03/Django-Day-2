from django.contrib import admin
from managedb.models import studentdetails


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "id", "first_name",'last_name','email','mobile_no','grade','faculty']

admin.site.register(studentdetails,CourseAdmin)