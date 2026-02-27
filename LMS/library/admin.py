from django.contrib import admin
from .models import Book, Student, IssuedBook
from .models import Book, Student, IssuedBook, WorkingDay

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
admin.site.register(WorkingDay)