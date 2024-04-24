from django.urls import path
from . import views
from .views import StudentListCreateView

from django.urls import path


urlpatterns = [
    path('dashboard/',views.dashboard),
    path('employee_view/',views.employee_view),
    path('addup/',views.addup),
    path('details/',views.details),
    path('edit_details/<int:id>/',views.edit_details),
    path('Delete_employee/',views.Delete_employee),
    path('modify/',views.modify),
    path('search/',views.search),
    path('book_master/',views.book_master),
    path('ui/',views.ui),
    path('add_book/',views.add_book),
    path('book_detail/',views.book_detail),
    path('edit_book_details/<int:id>/',views.edit_book_details),
    path('modify_book_details/',views.modify_book_details),
    path('delete_book/',views.delete_book),
    path('login_check/',views.login_check),
    path('',views.login_page),
    path('date_book_search_filter',views.date_book_search_filter),
    path('signup/',views.signup),
    path('signup_page/',views.signup_page),
    path('login_page/',views.login_page),
    path('logout/',views.logout),
    path('request_book/',views.request_book),
    path('issue_book/',views.issue_book),
    path('book_request/',views.book_request),
    path('book_edit_request/<int:id>/',views.book_edit_request),
    path('modify_issue_book/',views.modify_issue_book),
    path('delete_book1/',views.delete_book1),
    path('change_request_status/',views.change_request_status),
    path('daily_visitors1/',views.daily_visitors1),
    path('daily_book_request/',views.daily_book_request),
    path('add_book_request/',views.add_book_request),
    path('delete_book2/',views.delete_book2),
    path('edit_daily_bookrequest/<int:id>/',views.edit_daily_bookrequest),
    path('modify_daily_book/',views.modify_daily_book),
    path('change_request_daily_book_status/',views.change_request_daily_book_status),
    path('save_calculated_amount/',views.save_calculated_amount),
    path('Employee_Salary/',views.Employee_Salary),
    path('add_Emp_detail/',views.add_Emp_detail),
    path('Salary_page/',views.Salary_page),
    path('edit_emp_details/<int:id>/',views.edit_emp_details),
    path('modify_emp_detail/',views.modify_emp_detail),
    path('delete_emp_detail/',views.delete_emp_detail),
    path('Designation_select/',views.Designation_select),
    # path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('student_api/',views.student_api),
    path('students/', StudentListCreateView.as_view(), name='student-list-create')




    
    
    ]







