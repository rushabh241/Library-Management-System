from django.db import models

class student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    class_dept = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    def __str__(self):
        return f"{self.student_id}"
    
class book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.book_id}"

class issue_return(models.Model):
    student_id = models.IntegerField()
    book_id = models.IntegerField()
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    expected_return_date = models.DateField()

class history(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    class_dept = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    year = models.DateField()
