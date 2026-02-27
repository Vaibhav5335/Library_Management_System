# library/forms.py
from django import forms
from .models import Book, Student

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author', 'isbn']

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Student
        fields = ['name', 'student_id', 'email', 'phone_number']

class IssueBookForm(forms.Form):
    book_id = forms.IntegerField(label="Book ID ")
    student_id = forms.CharField(label="Student ID ")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class SearchForm(forms.Form):
    query = forms.IntegerField(label="Enter B.ID ")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class StudentSearchForm(forms.Form):
    query = forms.CharField(label="Enter S.ID ")

class WorkingCalendarUploadForm(forms.Form):
    excel_file = forms.FileField(label="Upload Working Days Calendar", widget=forms.FileInput(attrs={'accept': '.xlsx, .xls'}))

class WorkingCalendarUploadForm(forms.Form):
    excel_file = forms.FileField(
        label="Upload Working Days Calendar (Excel)",
        widget=forms.FileInput(attrs={'accept': '.xlsx, .xls'})
    )