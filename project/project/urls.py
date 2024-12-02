"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addStudent/', addStudent, name='addStudent'),
    path('addBook/', addBook, name='addBook'),
    path('callIssue/', callIssue, name='callIssue'),
    path('callReturn/', callReturn, name='callReturn'),
    path('call_manageStudent/', call_manageStudent, name='call_manageStudent'),
    path('manageStudent/', manageStudent, name='manageStudent'),
    path('studentDetails/<int:student_id>/', studentDetails, name='studentDetails'),
    path('updateStudent/', updateStudent, name='updateStudent'),
    path('call_manageBook/', call_manageBook, name='call_manageBook'),
    path('manageBook/', manageBook, name='manageBook'),
    path('bookDetails/<int:book_id>/', bookDetails, name='bookDetails'),
    path('updateBook/', updateBook, name='updateBook'),
    path('issuePage/', issuePage, name='issuePage'),
    path('issueInfo/<int:student_id>/', issueInfo, name='issueInfo'),
    path('issueBook/', issueBook, name='issueBook'),
    path('display_records/', display_records, name='display_records'),
    path('returnPage/', returnPage, name='returnPage'),
    path('returnInfo/<int:student_id>/', returnInfo, name='returnInfo'),
    path('returnBook/', returnBook, name='returnBook'),
    path('display_records_return/', display_records_return, name='display_records_return'),
    path('student_reports/', student_reports, name='student_reports'),
    path('book_reports/', book_reports, name='book_reports'),
    path('pending/', pending, name='pending'),
    path('delete_student/', delete_student, name='delete_student'),
    path('', include('app.urls')),
]
