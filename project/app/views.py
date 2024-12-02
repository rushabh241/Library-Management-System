from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import student, book, issue_return
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

#open issue book main page
def callIssue(request):
    return render(request, 'call_issue.html')

#open return book main page
def callReturn(request):
    return render(request, 'call_return.html')

#open manage student main page
def call_manageStudent(request):
    return render(request, 'manage_students.html')

#open manage student main page
def call_manageBook(request):
    return render(request, 'manage_books.html')

def addStudent(request):
    if request.method == 'POST':
        stud_name = request.POST['stud_name']
        print(stud_name)
        phone = request.POST['phone']
        print(phone)
        cls = request.POST['class']
        print(cls)
        roll = request.POST['roll']
        print(roll)

        form = student(student_name=stud_name,phone=phone,class_dept=cls,roll_no=roll)
        form.save()

        messages.success(request, 'Student record added successfully!')
        return redirect('addStudent')

    return render(request, 'add_student.html')
       
def addBook(request):
    if request.method == 'POST':
        bid = request.POST['book_id']
        bname = request.POST['book_name']
        sub = request.POST['subject']
        publisher = request.POST['publisher']
        auth_name = request.POST['author']

        form = book(book_id=bid, book_name=bname, subject=sub, publisher_name=publisher, author_name=auth_name)
        form.save()

        messages.success(request, 'Book added successfully!')
        return redirect('addBook')

    return render(request, 'add_book.html')

'''

Manage students starts here

'''

#student search button for manage students 
def manageStudent(request):
    search_class = request.GET.get('class') 
    print(search_class)
    class_object = student.objects.filter(class_dept=search_class).values()
    return render(request, 'manage_students.html', {'students': class_object})

#pass student id to next page from manage student
def studentDetails(request, student_id):
    student_obj = student.objects.filter(student_id=student_id).values()
    return render(request, 'students.html', {'student': student_obj})

#Update the student record
def updateStudent(request):
    if request.method == 'POST':
        student_id = request.POST.get('stud_id')
        name = request.POST.get('stud_name')
        phone = request.POST.get('phone')
        cls = request.POST.get('class')
        roll = request.POST.get('roll')

        # Check if student_id exists
        if student_id:
            try:
                student_instance = student.objects.get(student_id=student_id)
                # Update existing record
                student_instance.student_name = name
                student_instance.phone = phone
                student_instance.class_dept = cls
                student_instance.roll_no = roll
                student_instance.save()
            except student.DoesNotExist:
                # If student_id doesn't exist, create a new record
                student.objects.create(student_name=name, phone=phone, class_dept=cls, roll_no=roll)
        else:
            # If student_id is not provided, create a new record
            student.objects.create(student_name=name, phone=phone, class_dept=cls, roll_no=roll)

    return render(request, 'students.html')

'''

Manage Book Starts Here

'''

#open manage student main page
def call_manageBook(request):
    return render(request, 'manage_books.html')

#student search button for manage students  
def manageBook(request):
    book_name = request.GET.get('book_name') 
    print(book_name)
    book_name_object = book.objects.filter(book_name__contains=book_name).values()
    return render(request, 'manage_books.html', {'books': book_name_object})

#pass student id to next page from manage student
def bookDetails(request, book_id):
    book_obj = book.objects.filter(book_id=book_id).values()
    return render(request, 'books.html', {'book': book_obj})

def updateBook(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        name = request.POST.get('book_name') 
        sub = request.POST.get('subject')
        publisher = request.POST.get('publisher')
        author = request.POST.get('author')

        try:
            book_instance = book.objects.get(book_id=book_id)
            book_instance.book_name = name
            book_instance.subject = sub
            book_instance.publisher_name = publisher
            book_instance.author_name = author
            book_instance.save()
        except book.objects.get(book_id!=book_id):
            form = book(book_id=book_id, book_name=name, subject=sub, publisher_name=publisher, author_name=author)
            form.save()

    return render(request, 'books.html')

#display studend records in table
def issuePage(request):
    search_class = request.GET.get('class') 
    print(search_class)
    class_object = student.objects.filter(class_dept=search_class).values()
    return render(request, 'call_issue.html', {'students': class_object})

#fetching student_id and redirecting to student's personal page
def issueInfo(request, student_id):
    # Fetch the student object
    student_obj = student.objects.filter(student_id=student_id).values()
    return render(request, 'issue_book.html', {'student': student_obj})

#actual issue book logic
def issueBook(request):
    if request.method == 'POST':
        stud_id = request.POST.get('stud_id')
        bid = request.POST.get('book_id')
        
        # Check if the book is already issued to a student
        already_issued_book = issue_return.objects.filter(book_id=bid, return_date__isnull=True).exists()
        if already_issued_book:
            message = 'This book is already issued to a student. Please enter correct book id.'
            return render(request, 'issue_book.html', {'msg': message})
        
        # Check if the student has already issued a book
        already_issued_student = issue_return.objects.filter(student_id=stud_id, return_date__isnull=True).exists()
        if already_issued_student:
            message = 'You have already issued a book. Please return it!'
            return render(request, 'issue_book.html', {'msg': message})
         
        current_date = timezone.now().date()
        expected_return_date = current_date + timedelta(days=7)
        new_issue = issue_return.objects.create(student_id=stud_id, book_id=bid, issue_date=current_date, expected_return_date=expected_return_date)
        return render(request, 'issue_book.html', {'msg': 'Book issued successfully.'})
    
    book_id = request.GET.get('book_id')
    book_info = book.objects.filter(book_id=book_id).values()
    return render(request, 'issue_book.html', {'book_nm': book_info})

#to display the issued book records in table on same page
def display_records(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            issued_books = issue_return.objects.filter(student_id=student_id).order_by('-issue_date')
            return render(request, 'issue_book.html', {'issued_books': issued_books})
        else:
            return HttpResponse("Student ID is not provided.")
    return render(request, 'issue_book.html', {'issued_books': []})

#Return book starts here
def returnPage(request):
    search_class = request.GET.get('class') 
    print(search_class)
    class_object = student.objects.filter(class_dept=search_class).values()
    return render(request, 'call_return.html', {'students': class_object})

def returnInfo(request, student_id):
    student_obj = student.objects.filter(student_id=student_id).values()
    return render(request, 'return_book.html', {'student': student_obj})

def returnBook(request):
    if request.method == 'POST':
        stud_id = request.POST.get('stud_id')
        bid = request.POST.get('book_id')
        
        # Check if the book is issued to the student
        issued_book = issue_return.objects.filter(student_id=stud_id, book_id=bid, return_date__isnull=True).first()
        if issued_book:
            # Update the return date to today's date
            issued_book.return_date = timezone.now().date()
            issued_book.save()
            return render(request, 'return_book.html', {'msg': 'Book returned successfully.'})
        else:
            return render(request, 'return_book.html', {'msg': 'This book is not issued to you.'})
    
    return render(request, 'return_book.html')

def display_records_return(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            issued_books = issue_return.objects.filter(student_id=student_id).order_by('-issue_date')
            return render(request, 'return_book.html', {'issued_books': issued_books})
        else:
            return HttpResponse("Student ID is not provided.")
    return render(request, 'return_book.html', {'issued_books': []})

def student_reports(request):
    students = student.objects.all().order_by('class_dept')
    total_students = students.count()
    return render(request, 'student_reports.html', {'students': students, 'total_students': total_students})

def book_reports(request):
    books = book.objects.all()  # Fetching all book objects
    total_books = books.count()  # Counting the total number of books
    return render(request, 'book_reports.html', {'books': books, 'total_books': total_books})

def pending(request):
    pending_student_ids = issue_return.objects.filter(return_date__isnull=True).values_list('student_id', flat=True)
    pending_students = student.objects.filter(student_id__in=pending_student_ids)
    
    pending_books = fetch_book_details_for_pending_returns()
    
    return render(request, 'pending.html', {'pending_students': pending_students, 'pending_books': pending_books})

def fetch_book_details_for_pending_returns():


    # Retrieve book details for pending returns
    pending_books = []
    for pending_return in issue_return.objects.filter(return_date__isnull=True):
        book_id = pending_return.book_id
        book_name = book.objects.get(book_id=book_id).book_name
        pending_books.append({'student_id': pending_return.student_id, 'book_id': book_id, 'book_name': book_name})
    
    return pending_books

def delete_student(request):
    if request.method == 'POST':
        stud_name = request.POST['stud_name']
        cls = request.POST['class']
        roll = request.POST['roll']
        try:
            student_obj = student.objects.get(student_name=stud_name, class_dept=cls, roll_no=roll)
            student_obj.delete()
            messages.success(request, 'Student record deleted successfully!')
            return redirect('delete_student')  # Redirect to the delete_student page
        except student.DoesNotExist:
            return render(request, 'error_page.html', {'message': 'Student record not found'})

    return render(request, 'delete_student.html')