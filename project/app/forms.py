from django import forms
from .models import student, book, issue_return

class book_dtls(forms.ModelForm):
    class Meta:
        model = book
        fields = ['book_id', 'book_name', 'subject', 'publisher_name', 'author_name', 'available_quantity']

class stud_dtls(forms.ModelForm):
    class Meta:
        model = student
        fields = ['student_id', 'student_name', 'phone', 'class', 'roll_no', ]

class issueBook(forms.ModelForm):
    class Meta:
        model = issue_return
        fields = ['student_id', 'book_id', 'issue_date', 'return_date', 'expected_return_date']