from django.db import models
from django.utils import timezone
import datetime

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Enter 10-digit phone number')

    def __str__(self):
        return f"{self.name} ({self.student_id})"

# library/models.py

class Book(models.Model):
    book_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, help_text='13 Character ISBN number')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (ID: {self.book_id})"

class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE) # One book can be issued to one student at a time
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book.title} issued to {self.student.name}"

    def save(self, *args, **kwargs):
        # Set the return date to 15 days from the issue date by default
        if not self.return_date:
            self.return_date = timezone.now().date() + datetime.timedelta(days=15)
        super().save(*args, **kwargs)

class WorkingDay(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")