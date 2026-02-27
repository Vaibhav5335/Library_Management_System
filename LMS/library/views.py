# library/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from django.db import IntegrityError
import datetime
import pandas as pd

from .models import Book, Student, IssuedBook
from .forms import BookForm, StudentForm, IssueBookForm, SearchForm, StudentSearchForm
from .models import Book, Student, IssuedBook, WorkingDay
from .forms import WorkingCalendarUploadForm

# --- Main Dashboard ---
def home(request):
    book_count = Book.objects.count()
    student_count = Student.objects.count()
    issued_book_count = IssuedBook.objects.count()
    context = {
        'book_count': book_count,
        'student_count': student_count,
        'issued_book_count': issued_book_count,
    }
    return render(request, 'library/home.html', context)

# --- Book Management ---
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def view_books(request):
    books = Book.objects.all()
    return render(request, 'library/view_books.html', {'books': books})

def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if not book.is_available:
        messages.error(request, f'Cannot delete "{book.title}" because it is currently issued.')
        return redirect('view_books')
    if request.method == 'POST':
        book.delete()
        messages.success(request, f'Book "{book.title}" has been deleted successfully.')
        return redirect('view_books')
    return render(request, 'library/delete_book_confirm.html', {'book': book})

# --- Student Management ---
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully!')
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'library/add_student.html', {'form': form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'library/view_students.html', {'students': students})

def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            student_id = form.cleaned_data['student_id']
            try:
                book = Book.objects.get(book_id=book_id, is_available=True)
                student = Student.objects.get(student_id=student_id)
                
                issue_date = timezone.now().date()
                # Default period: 28 days from issue
                provisional_return_date = issue_date + datetime.timedelta(days=28)
                
                # Check if the provisional date is a working day
                if not WorkingDay.objects.filter(date=provisional_return_date).exists():
                    # Find the next working day after the provisional date
                    next_days_qs = WorkingDay.objects.filter(date__gt=provisional_return_date).order_by('date')
                    if next_days_qs.exists():
                        provisional_return_date = next_days_qs.first().date
                # Create the issued book record with the computed return date
                IssuedBook.objects.create(
                    book=book,
                    student=student,
                    return_date=provisional_return_date
                )
                book.is_available = False
                book.save()
                messages.success(request, f'Book "{book.title}" issued until {provisional_return_date}.')
                return redirect('view_issued_books')
            except Book.DoesNotExist:
                messages.error(request, 'Book is not available or does not exist.')
            except Student.DoesNotExist:
                messages.error(request, 'Student does not exist.')
    else:
        form = IssueBookForm()
    return render(request, 'library/issue_book.html', {'form': form})

def view_issued_books(request):
    issued_books = IssuedBook.objects.all()
    return render(request, 'library/view_issued_books.html', {'issued_books': issued_books})

def return_book(request, issued_book_id):
    issued_book = get_object_or_404(IssuedBook, id=issued_book_id)
    book = issued_book.book
    book.is_available = True
    book.save()
    issued_book.delete()
    messages.success(request, f'Book "{book.title}" has been returned.')
    return redirect('view_issued_books')

def reissue_book(request, issued_book_id):
    issued_book = get_object_or_404(IssuedBook, id=issued_book_id)
    issued_book.return_date = timezone.now().date() + datetime.timedelta(days=15)
    issued_book.save()
    messages.success(request, f'Due date for "{issued_book.book.title}" has been extended.')
    return redirect('view_issued_books')

# --- Search Functionality ---
def search_book(request):
    book = None
    issue_info = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            try:
                book = Book.objects.get(book_id=query)
                if not book.is_available:
                    issue_info = IssuedBook.objects.get(book=book)
            except Book.DoesNotExist:
                messages.error(request, 'No book found with the given ID.')
    else:
        form = SearchForm()
    return render(request, 'library/search_book.html', {'form': form, 'book': book, 'issue_info': issue_info})

def search_student(request):
    student = None
    issued_books = None
    if 'query' in request.GET:
        form = StudentSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            try:
                student = Student.objects.get(student_id=query)
                issued_books = IssuedBook.objects.filter(student=student)
            except Student.DoesNotExist:
                messages.error(request, 'No student found with the given ID.')
    else:
        form = StudentSearchForm()
    return render(request, 'library/search_student.html', {'form': form, 'student': student, 'issued_books': issued_books})

# --- Bulk Uploads ---
def upload_books(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if not excel_file:
            messages.error(request, 'No file was uploaded.')
            return redirect('upload_books')
        try:
            df = pd.read_excel(excel_file)
            success_count = 0
            failed_records = []
            for index, row in df.iterrows():
                try:
                    Book.objects.create(book_id=row['Book ID'], title=row['Title'], author=row['Author'], isbn=row['ISBN'])
                    success_count += 1
                except IntegrityError:
                    failed_records.append(f"Row {index+2}: Book with this ID or ISBN already exists.")
                except Exception as e:
                    failed_records.append(f"Row {index+2}: {str(e)}")
            messages.success(request, f'Successfully imported {success_count} books.')
            for error in failed_records:
                messages.error(request, error)
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}. Make sure the column headers are correct.')
        return redirect('view_books')
    context = {'title': 'Upload Books from Excel', 'sample_format': 'Book ID | Title | Author | ISBN', 'cancel_url': request.build_absolute_uri(reverse('view_books'))}
    return render(request, 'library/upload_form.html', context)

def upload_students(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if not excel_file:
            messages.error(request, 'No file was uploaded.')
            return redirect('upload_students')
        try:
            df = pd.read_excel(excel_file)
            success_count = 0
            failed_records = []
            for index, row in df.iterrows():
                try:
                    Student.objects.create(name=row['Name'], student_id=row['Student ID'], email=row['Email'])
                    success_count += 1
                except IntegrityError:
                    failed_records.append(f"Row {index+2}: Student with this ID or Email already exists.")
                except Exception as e:
                    failed_records.append(f"Row {index+2}: {str(e)}")
            messages.success(request, f'Successfully imported {success_count} students.')
            for error in failed_records:
                messages.error(request, error)
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}. Make sure the column headers are correct.')
        return redirect('view_students')
    context = {'title': 'Upload Students from Excel', 'sample_format': 'Name | Student ID | Email', 'cancel_url': request.build_absolute_uri(reverse('view_students'))}
    return render(request, 'library/upload_form.html', context)

# --- Notifications Page ---
def view_notifications(request):
    return render(request, 'library/notifications.html')

# library/views.py (add this new view somewhere)
def upload_working_calendar(request):
    from .forms import WorkingCalendarUploadForm  # if not imported already
    if request.method == 'POST':
        form = WorkingCalendarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES.get('excel_file')
            import pandas as pd
            try:
                # Read the file into a DataFrame
                df = pd.read_excel(excel_file)
                # Assume the Excel has one column named "Date" in Y-m-d format.
                success_count = 0
                errors = []
                for index, row in df.iterrows():
                    try:
                        # Create (or update) working day records.
                        d = row['Date']
                        # Ensure d is a date (pandas may read as Timestamp)
                        WorkingDay.objects.update_or_create(date=d)
                        success_count += 1
                    except Exception as e:
                        errors.append(f"Row {index+2}: {str(e)}")
                messages.success(request, f'Successfully processed {success_count} working day entries.')
                for error in errors:
                    messages.error(request, error)
            except Exception as ex:
                messages.error(request, f"Error reading file: {str(ex)}")
            return redirect('view_working_calendar')  # You can create a view to list all working days.
    else:
        form = WorkingCalendarUploadForm()
    return render(request, 'library/upload_working_calendar.html', {'form': form})

def upload_working_calendar(request):
    """
    Bulk upload working days from an Excel file.
    The Excel file must include a column with the header "Date".
    """
    if request.method == 'POST':
        form = WorkingCalendarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES.get('excel_file')
            try:
                # Read Excel file into a DataFrame.
                # Make sure your Excel file has one column labeled "Date"
                df = pd.read_excel(excel_file)
                success_count = 0
                errors = []
                for index, row in df.iterrows():
                    try:
                        # Assuming the Excel file column header is exactly "Date"
                        working_date = row['Date']
                        # update_or_create prevents duplicates if the date is already present.
                        WorkingDay.objects.update_or_create(date=working_date)
                        success_count += 1
                    except Exception as e:
                        errors.append(f"Row {index+2}: {str(e)}")
                messages.success(request, f"Successfully processed {success_count} working day entries.")
                for error in errors:
                    messages.error(request, error)
            except Exception as ex:
                messages.error(
                    request,
                    f"Error reading file: {str(ex)}. Ensure the file has a column 'Date'."
                )
            # Redirect to a page listing working days or the home page.
            return redirect('view_working_calendar')
    else:
        form = WorkingCalendarUploadForm()
    return render(request, 'library/upload_working_calendar.html', {'form': form})

def view_working_calendar(request):
    working_days = WorkingDay.objects.order_by('date')
    return render(request, 'library/view_working_calendar.html', {'working_days': working_days})