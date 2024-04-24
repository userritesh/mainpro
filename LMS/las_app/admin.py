from django.contrib import admin
from .models import *



class User_admin(admin.ModelAdmin):
    list_display =("id","Employee_Name" ,"Email" ,"Designation" ,"DOJ")
admin.site.register(UserDetails,User_admin )


class Book_admin(admin.ModelAdmin):
    list_display = ("id", "Book", "Author", "DOP", "Condition", "per_day_Price","per_hour_Price")

admin.site.register(BookDetails, Book_admin)


class check_admin(admin.ModelAdmin):  
    list_display = ("id", "Email", "Password")
    
admin.site.register(CkeckDetails, check_admin)


class IssueBookAdmin(admin.ModelAdmin):
    list_display = ("id", "Book_Name", "Student_Name", "Stu_Class",  "Section", "Email", "Issue_Date", "Till_Date","Charge", "Condition", "Request_Status","img")

admin.site.register(IssueBook, IssueBookAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","Employee_Name","destination","yearly_package","monthly_salary","Designation")

admin.site.register(Employee, EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","name","roll_no","city",)

admin.site.register(Student, StudentAdmin)
