from inspect import _Traceback
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from datetime import  datetime






from .models import UserDetails 
from .models import BookDetails 
from .models import CkeckDetails 
from .models import IssueBook 
from .models import daily_visitors 
from .models import Employee 


from django.conf import settings
from django.core.mail import send_mail


@csrf_exempt
def logout(request):
    if request.session.get('user_id'):
        del request.session['user_id']
        # return HttpResponse("success")
    # else:
        return redirect('/')

def dashboard(request):
    if request.session.get('user_id'):
        return render(request,'website/dashboard.html')
    else:
        return redirect('/')

def employee_view(request):
    if request.session.get('user_id'):
        obj2 = UserDetails.objects.all()
        return render(request,'website/employee.html',{"obj2":obj2})
    else:
        return redirect('/')
    
def addup(request):
    return render(request,'website/add_employee.html',{"type":"add"})

@csrf_exempt
def details(request):
    
    name = request.POST.get('name')
    email =request.POST.get('email')
    designation = request.POST.get('designation')
    doj = request.POST.get('doj')
    print(email,name)
                
    UserDetails.objects.create(Employee_Name=name,Email=email,Designation=designation,DOJ=doj)  
    return HttpResponse("success")

def edit_details(request,id):
    obj2 = UserDetails.objects.get(id=id)
    return render(request,'website/add_employee.html',{"obj2":obj2})

# @csrf_exempt   
# def Delete_employee(request):
#     id = request.POST.get("id")
#     obj2 = UserDetails.objects.get(id=id)
#     obj2.delete()

#     return HttpResponse("success")  


@csrf_exempt
def Delete_employee(request):
    id = request.POST.get('id')
    obj2 = UserDetails.objects.get(id=id)
    obj2.delete()
    return HttpResponse("success")



@csrf_exempt
def modify(request):    
    name=request.POST.get("name")
    email = request.POST.get("email")
    designation =request.POST.get("designation")
    doj =request.POST.get("doj")
    objId =request.POST.get("objId")
    
    obj2 = UserDetails.objects.get(id=objId)
    obj2.Employee_Name=name
    obj2.Email=email
    obj2.Designation=designation
    obj2.DOJ=doj
    print(email,name)

    obj2.save()
    return HttpResponse("success")


@csrf_exempt
def search(request):
    first_date = request.POST.get("first_date")
    last_date = request.POST.get("last_date")

    print(first_date,last_date)
    obj1 = UserDetails.objects.filter(DOJ__gte = first_date,DOJ__lte = last_date).order_by('-DOJ')
    print(obj1)
    rendered = render_to_string('website/r_t_s_employee.html',{'first_date':first_date,'last_date':last_date,'obj1':obj1})
    return JsonResponse({"status":1, "data":rendered})

def book_master(request):
     if request.session.get('user_id'):
        book_obj =BookDetails.objects.all()
        return render(request,'website/book_master.html',{"book_obj":book_obj})
     else:
        return redirect('/')
     
def ui(request):
    return render(request,'website/ui.html')

def add_book(request):
    return render(request,'website/add_Book.html',{"type":"add_book"})

@csrf_exempt
def book_detail(request):
    Book = request.POST.get("Book")
    Author = request.POST.get("Author")
    DOP = request.POST.get("DOP")
    Condition = request.POST.get("Condition")
    Price = request.POST.get("Price")
    print(Book,Author)
    BookDetails.objects.create(Book=Book,Author=Author,DOP=DOP,Condition=Condition,Price=Price)
    return HttpResponse("success")


def edit_book_details(request, id):
    book_obj = BookDetails.objects.get(id=id)
    return render(request, 'website/add_Book.html', {'book_obj': book_obj})

@csrf_exempt
def modify_book_details(request):
    Book = request.POST.get("Book")
    Author = request.POST.get("Author")
    DOP = request.POST.get("DOP")
    Condition = request.POST.get("Condition")
    Price = request.POST.get("Price")
    book_id = request.POST.get("book_id")
    print(Book,Author)
    book_obj = BookDetails.objects.get(id=book_id)

    book_obj.Book =Book
    book_obj.Author=Author
    book_obj.DOP=DOP
    book_obj.Condition=Condition
    book_obj.Price=Price
    book_obj.save()
    return HttpResponse("success")

@csrf_exempt
def delete_book(request):
    book_id=request.POST.get("id")
    book_obj = BookDetails.objects.filter(id=book_id)
    book_obj.delete()
    return HttpResponse("success")
 

def login_page(request):
     return render(request,'website/login.html')

def signup_page(request):
     return render(request,'website/signup.html')

@csrf_exempt
def login_check(request):
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        if CkeckDetails.objects.filter(Email=Email, Password=Password).exists():
            user = CkeckDetails.objects.get(Email=Email, Password=Password)
            request.session['user_id']=str(user.id)
            return HttpResponse("success")
        else:
            return HttpResponse("error")



@csrf_exempt
def date_book_search_filter(request):
    first_date = request.POST.get("first_date")
    last_date = request.POST.get("last_date")
    book_obj = BookDetails.objects.filter(DOP__gte = first_date,DOP__lte = last_date).order_by('-DOP')
    print(book_obj)
    rendered = render_to_string('website/r_t_s_book.html.html',{'first_date':first_date,'last_date':last_date,'book_obj':book_obj})
    return JsonResponse({"status":1, "data":rendered})

# def book_master(request):
#     book_obj =BookDetails.objects.all()
#     return render(request,'website/book_master.html',{"book_obj":book_obj})

@csrf_exempt           
def signup(request):    

    User_Name = request.POST.get("User_Name")
    Email = request.POST.get("Email")
    PhoneNumber = request.POST.get("PhoneNumber")
    Password = request.POST.get("Password")
    
    print(User_Name,Email,PhoneNumber,Password)
    
    # UserDetails.objects.create(email=email,Password=Password,fname="fname",lname="lname")
    obj = CkeckDetails.objects.create( User_Name=User_Name, Email=Email, PhoneNumber=PhoneNumber,Password=Password)
    request.session['user_id'] = obj.id
    return HttpResponse("success")

def issue_book(request):
    if request.session.get('user_id'):
        current_date = datetime.now().date()

        for i in IssueBook.objects.all():
            Till_Date = i.Till_Date
            if Till_Date:
                diff =  current_date- Till_Date
                print(diff,'...........')
                if diff.days > 0:
                    book_price = BookDetails.objects.get(id=i.Book_Name.id)
                    charge = diff.days * int(book_price.per_day_Price)
                    print(charge)
                    i.Charge = charge
                    i.save()

                else:
                    i.Charge = 0
                    i.save()
      
        obj3= IssueBook.objects.all()
        return render(request,'website/book_issue_status.html',{"obj3":obj3,"book_price":book_price})
    else:
        return redirect('/')


def request_book(request):
    obj_book= BookDetails.objects.all().order_by("id")
    obj_user= UserDetails.objects.all().order_by("id")
    
    return render(request,'website/request_book.html',{"obj_book": obj_book,"obj_user" :obj_user,"type":"add_book"})

@csrf_exempt           
def book_request(request):
    Book_Name = request.POST.get('Book_Name')
    Student_Name =request.POST.get('Student_Name')
    Stu_Class = request.POST.get('Stu_Class')
    Section = request.POST.get('Section')
    Email = request.POST.get('Email')
    Issue_Date = request.POST.get('Issue_Date')
    Till_Date = request.POST.get('Till_Date')
    # Charge = request.POST.get('Charge')
    Condition= request.POST.get('Condition')
    Request_Status=request.POST.get('Request_Status')
    img = request.FILES.get('img')
    # Request_genrated_by = request.POST.get('Request_genrated_by') 
    request_generated_by = request.POST.get('Request_genrated_by')

    print(Book_Name,Student_Name)

    IssueBook.objects.create(Book_Name_id=Book_Name, Student_Name=Student_Name, Stu_Class=Stu_Class,Section=Section,Email=Email, Issue_Date=Issue_Date, Till_Date=Till_Date,Condition=Condition,Request_Status="pending",img=img,fk_employee_id=request_generated_by)
    return HttpResponse("success")


def book_edit_request(request,id):
    obj_issuebook = IssueBook.objects.get(id=id)
    obj_book= BookDetails.objects.all().order_by("id")
    obj_user= UserDetails.objects.all().order_by("id")
    return render(request,'website/edit_issuebook.html',{"obj3":obj_issuebook, "obj_book":obj_book, "obj_user":obj_user})

@csrf_exempt           
def modify_issue_book(request):
    Book_Name = request.POST.get('Book_Name')
    Student_Name =request.POST.get('Student_Name')
    Stu_Class = request.POST.get('Stu_Class')
    Section = request.POST.get('Section')
    Email = request.POST.get('Email')
    Issue_Date = request.POST.get('Issue_Date')
    Till_Date = request.POST.get('Till_Date')
    # Charge = request.POST.get('Charge')
    Condition= request.POST.get('Condition')
    Request_Status=request.POST.get('Request_Status')
    img = request.FILES.get('img')
    Request_genrated_by = request.POST.get('Request_genrated_by') 
    # Charge=Charge,
    print(Request_genrated_by)

    issue_id = request.POST.get("issue_id")

    issue_obj = IssueBook.objects.get(id=issue_id)
    issue_obj.Book_Name_id=Book_Name
    issue_obj.Student_Name=Student_Name
    issue_obj.Stu_Class=Stu_Class
    issue_obj.Section=Section
    issue_obj.Email=Email
    issue_obj.Issue_Date=Issue_Date
    issue_obj.Till_Date=Till_Date
    issue_obj.Condition=Condition
    if img:
        issue_obj.img=img
    else:
        pass
    issue_obj.fk_employee_id=Request_genrated_by 
    issue_obj.save()
    
    return HttpResponse("success")


@csrf_exempt
def delete_book1(request):
    id=request.POST.get("id")
    issue_obj = IssueBook.objects.filter(id=id)
    issue_obj.delete()
    return HttpResponse("success")

@csrf_exempt    
def change_request_status(request):
    id = request.POST.get("id")
    Request_Status = request.POST.get("Request_Status")
    
    # obj = IssueBook.objects.get(id = id)
    # obj.Request_Status = Request_Status
    # obj.save()
    # return HttpResponse("success") 
    
    if IssueBook.objects.filter(id = id).exists():
        
        obj = IssueBook.objects.get(id = id)
        obj.Request_Status = Request_Status
        obj.save()
        print(id)
        print(Request_Status)
        
        if Request_Status == "Accept":
          
          message = 'your request has been accepetd'
        else:
          message = 'your request has been rejected'
        
        try:
            subject = 'welcome to library management'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["meshramritesh98@gmail.com" ]
            send_mail( subject, message, email_from, recipient_list )
          
            return HttpResponse("success") 
            
        except:
            # print(_Traceback.print_exc())
            return HttpResponse("error") 
        
    else:
        return HttpResponse("error") 


    
@csrf_exempt    
def daily_visitors1(request):
    if request.session.get('user_id'):
    #     current_time = timezone.now()

    #     for i in daily_visitors.objects.all():
    #         Issue_Time = i.Issue_Time
    #         Time_Period =  current_time - Issue_Time
    #         print(Time_Period,'...........')
    #         if Time_Period.days > 0:
    #             book_price = BookDetails.objects.get(id=i.Book_Name.id)
    #             charge = Time_Period.days * int(book_price.Price)
    #             print(charge)
    #             i.Time_Period
    #             i.Charge = charge
    #             i.save()

    #         else:
    #             i.Charge = 0
    #             i.save()
        #                                     #    "book_price":book_price            
        obj_daily= daily_visitors.objects.all()
        return render(request,'website/daily_visitors.html',{"obj_daily":obj_daily,})
        # return render(request,'website/daily_visitors.html')

    else:
        return redirect('/')


def daily_book_request(request):
    obj_book= BookDetails.objects.all().order_by("id")
    obj_user= UserDetails.objects.all().order_by("id")


    return render(request,'website/daily_book_request.html',{"obj_book": obj_book,"obj_user" :obj_user,"type":"add_book",})

    
    # return render(request,'website/daily_book_request.html')

@csrf_exempt    
def add_book_request(request):
    Book_Name = request.POST.get('Book_Name')
    Student_Name =request.POST.get('Student_Name')
    Stu_Class = request.POST.get('Stu_Class')
    Section = request.POST.get('Section')
    Email = request.POST.get('Email')
    Issue_Time = request.POST.get('Issue_Time')
    Till_Time = request.POST.get('Till_Time')
    # Charge = request.POST.get('Charge')
    Condition= request.POST.get('Condition')
    Request_Status=request.POST.get('Request_Status')
    img = request.FILES.get('img')
    # Request_genrated_by = request.POST.get('Request_genrated_by') 
    request_generated_by = request.POST.get('Request_genrated_by')

    print(Book_Name,Student_Name)
    daily_visitors.objects.create(Book_Name_id=Book_Name, Student_Name=Student_Name, Stu_Class=Stu_Class,Section=Section,Email=Email,Issue_Time=Issue_Time,Till_Time=Till_Time,Condition=Condition,Request_Status="pending",img=img,fk_employee_id=request_generated_by)
    return HttpResponse("success")

@csrf_exempt    
def delete_book2(request):
    id=request.POST.get("id")
    daily_obj = daily_visitors.objects.filter(id=id)
    daily_obj.delete()
    return HttpResponse("success")

def edit_daily_bookrequest(request,id):
    daily_obj = daily_visitors.objects.get(id=id)
    obj_book= BookDetails.objects.all().order_by("id")
    obj_user= UserDetails.objects.all().order_by("id")

    return render(request,'website/daily_book_request.html',{"daily_obj":daily_obj,"obj_book":obj_book,"obj_user":obj_user})

@csrf_exempt    
def modify_daily_book(request):
    Book_Name = request.POST.get('Book_Name')
    Student_Name =request.POST.get('Student_Name')
    Stu_Class = request.POST.get('Stu_Class')
    Section = request.POST.get('Section')
    Email = request.POST.get('Email')
    Issue_Time = request.POST.get('Issue_Time')
    Till_Time = request.POST.get('Till_Time')
    # Charge = request.POST.get('Charge')
    Condition= request.POST.get('Condition')
    Request_Status=request.POST.get('Request_Status')
    img = request.FILES.get('img')
    Request_genrated_by = request.POST.get('Request_genrated_by') 
    # Charge=Charge,
    print(Request_genrated_by)

    daily_id = request.POST.get("daily_id")

    issue_obj = daily_visitors.objects.get(id=daily_id)
    issue_obj.Book_Name_id=Book_Name
    issue_obj.Student_Name=Student_Name
    issue_obj.Stu_Class=Stu_Class
    issue_obj.Section=Section
    issue_obj.Email=Email
    issue_obj.Issue_Time=Issue_Time
    issue_obj.Till_Time=Till_Time
    issue_obj.Condition=Condition
    if img:
        issue_obj.img=img
    else:
        pass
    issue_obj.fk_employee_id=Request_genrated_by 
    issue_obj.save()
    
    return HttpResponse("success")


@csrf_exempt    
def change_request_daily_book_status(request):
    id = request.POST.get("id")
    Request_Status = request.POST.get("Request_Status")
    
    # obj = IssueBook.objects.get(id = id)
    # obj.Request_Status = Request_Status
    # obj.save()
    # return HttpResponse("success") 
    
    if daily_visitors.objects.filter(id = id).exists():
        
        obj = daily_visitors.objects.get(id = id)
        obj.Request_Status = Request_Status
        obj.save()
        print(id)
        print(Request_Status)
        
        if Request_Status == "Accept":
          
          message = 'your request has been accepetd'
        else:
          message = 'your request has been rejected'
        
        try:
            subject = 'welcome to library management'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["meshramritesh98@gmail.com" ]
            send_mail( subject, message, email_from, recipient_list )
          
            return HttpResponse("success") 
            
        except:
            # print(_Traceback.print_exc())
            return HttpResponse("error") 
        
    else:
        return HttpResponse("error") 
    
@csrf_exempt    
def save_calculated_amount(request):
        modal_Issue_Time = request.POST.get('modal_Issue_Time')
        Till_Time =request.POST.get('Till_Time')
        Amount = request.POST.get('Amount')
        daily_id = request.POST.get('daily_id')
        
        issue_obj = daily_visitors.objects.get(id=daily_id)
        issue_obj.Charge = float(Amount) 
        issue_obj.save()
        return HttpResponse("success")
                  


def Employee_Salary(request):
    obj_emp = Employee.objects.all().order_by("id")
    obj2 = UserDetails.objects.all().order_by("id")

    return render(request, 'website/Employee_Salary.html', {'obj_emp': obj_emp,"obj2":obj2})


@csrf_exempt    
def add_Emp_detail(request):

    Employee_Name  = request.POST.get("Employee_Name")
    destination    = request.POST.get("destination")
    yearly_package = request.POST.get("yearly_package")
    monthly_salary = request.POST.get("monthly_salary")
    Designation = request.POST.get("Designation")
    print(Employee_Name,destination,Designation)
    Employee.objects.create(Employee_Name_id=Employee_Name,destination =destination ,yearly_package = yearly_package ,monthly_salary=monthly_salary,Designation=Designation)
    return HttpResponse("success") 


def Salary_page(request):
    obj2 = UserDetails.objects.all()

    return render(request,'website/Salary_page.html',{"type":"add_emp", "obj2":obj2,})


def edit_emp_details(request,id):
    obj_emp = Employee.objects.get(id=id)
    obj2 = UserDetails.objects.all()

    return render(request, 'website/Salary_page.html', {'obj_emp': obj_emp,"obj2":obj2})



@csrf_exempt
def modify_emp_detail(request):
        # Employee_Name=UserDetails.objects.get(id=Employee_Name.id)
    #    employee_name_instance = UserDetails.objects.get(id=employee_name_id)

        Employee_Name = request.POST.get("Employee_Name")
        destination = request.POST.get("destination")
        yearly_package = request.POST.get("yearly_package")
        monthly_salary = request.POST.get("monthly_salary")
        Designation = request.POST.get("Designation")
        emp_id = request.POST.get("emp_id")
        obj2 = Employee.objects.get(id=emp_id)
         
        obj2.Employee_Name_id = Employee_Name
        obj2.destination = destination
        obj2.yearly_package = yearly_package
        obj2.monthly_salary = monthly_salary
        obj2.Designation = Designation
        obj2.save()

        return HttpResponse("success")


@csrf_exempt    
def delete_emp_detail(request):
    id=request.POST.get("id")
    obj_emp = Employee.objects.filter(id=id)
    obj_emp.delete()
    return HttpResponse("success")

@csrf_exempt
def Designation_select(request):
    Employee_Name = request.POST.get("Employee_Name")
    user_details_obj = UserDetails.objects.get(id=Employee_Name)
     # Update the Designation_id field
    Designation = user_details_obj.Designation
    return JsonResponse({"status":1, "designation":Designation})


# api/views.py

from .models import Student
# from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def student_api(request):
    return Response({'message': 'Hello, World!'})


from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
