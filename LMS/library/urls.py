# library/urls.py
from django.urls import path
from . import views
from library.forms import BookForm, StudentForm, IssueBookForm, SearchForm, StudentSearchForm

urlpatterns = [
    path('', views.home, name='home'),
    
    path('add_book/', views.add_book, name='add_book'),
    path('view_books/', views.view_books, name='view_books'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
    path('add_student/', views.add_student, name='add_student'),
    path('view_students/', views.view_students, name='view_students'),

    path('upload/books/', views.upload_books, name='upload_books'),
    path('upload/students/', views.upload_students, name='upload_students'),
    
    path('issue_book/', views.issue_book, name='issue_book'),
    path('view_issued_books/', views.view_issued_books, name='view_issued_books'),
    path('return_book/<int:issued_book_id>/', views.return_book, name='return_book'),
    path('reissue_book/<int:issued_book_id>/', views.reissue_book, name='reissue_book'),
    
    path('search/', views.search_book, name='search_book'),
    path('search_student/', views.search_student, name='search_student'),

    path('notifications/', views.view_notifications, name='notifications'),

    path('upload/working-calendar/', views.upload_working_calendar, name='upload_working_calendar'),
    
    path('view/working-calendar/', views.view_working_calendar, name='view_working_calendar'),
]