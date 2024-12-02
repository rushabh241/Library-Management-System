from django.contrib import admin
from .models import book, student, issue_return


class MemberAdmin(admin.ModelAdmin):
  list_display = ("student_id", "student_name", "phone", "class_dept", "roll_no")
admin.site.register(student, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("book_id", "book_name", "subject", "publisher_name", "author_name")
admin.site.register(book, MemberAdmin)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("student_id", "book_id", "issue_date", "return_date", "expected_return_date")
admin.site.register(issue_return, MemberAdmin)

