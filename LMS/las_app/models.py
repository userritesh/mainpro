from django.db import models

class UserDetails(models.Model):
    Employee_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Designation = models.CharField(max_length=100, null=True, blank=True)
    DOJ = models.DateField(max_length=50)

class BookDetails(models.Model):
    Book = models.CharField(max_length=100, null=True, blank=True)
    Author =models.CharField(max_length=100, null=True, blank=True)
    DOP = models.DateField(max_length=50)
    Condition =models.CharField(max_length=100, null=True, blank=True)
    per_day_Price = models.CharField(max_length=100, null=True, blank=True)
    per_hour_Price = models.CharField(max_length=100, null=True, blank=True)
   
class CkeckDetails(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)    
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class IssueBook(models.Model):
    Book_Name = models.ForeignKey(BookDetails, on_delete=models.CASCADE, null=True, blank=True)
    fk_employee = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    Student_Name = models.CharField(max_length=100, null=True, blank=True)
    Stu_Class = models.CharField(max_length=100, null=True, blank=True)
    Section =models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Issue_Date = models.DateField(null=True, blank=True)
    Till_Date = models.DateField(null=True, blank=True)
    Charge = models.IntegerField(null=True, blank=True)
    Condition = models.CharField(max_length=100, null=True, blank=True)
    Request_Status = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    Request_genrated_by = models.CharField(max_length=100, null=True, blank=True)

class daily_visitors(models.Model):
    Book_Name = models.ForeignKey(BookDetails, on_delete=models.CASCADE,null=True, blank=True)
    Student_Name = models.CharField(max_length=100, null=True, blank=True)
    fk_employee = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    Stu_Class = models.CharField(max_length=100, null=True, blank=True)
    Section =models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Issue_Time = models.TimeField(null=True, blank=True)
    Till_Time = models.TimeField(null=True, blank=True)
    Charge = models.IntegerField(null=True, blank=True)
    Condition = models.CharField(max_length=100, null=True, blank=True)
    Return_Book = models.CharField(max_length=100, null=True, blank=True)
    Request_genrated_by = models.CharField(max_length=100, null=True, blank=True)


class Employee(models.Model):
    Employee_Name = models.ForeignKey(UserDetails,null = True,on_delete=models.CASCADE)
    destination=models.CharField(max_length=50, null=True, blank=True)
    yearly_package=models.IntegerField(null=True, blank=True)
    monthly_salary=models.CharField(max_length=50, null=True, blank=True)
    Designation=models.CharField(max_length=50, null=True, blank=True)

class Student(models.Model):
    name    = models.CharField(max_length=100, null=True, blank=True)
    roll_no = models.IntegerField()
    city    = models.CharField(max_length=100, null=True, blank=True)

