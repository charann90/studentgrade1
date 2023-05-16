from django.db import models

# Create your models here.
class Grades(models.Model):
    student_name=models.CharField(max_length=50)
    class_name=models.CharField(max_length=5)
    grade=models.CharField(max_length=1)
    marks=models.IntegerField()
    # #def __init__(self, student_name, class_name, grade):
    #     self.student_name = student_name
    #     self.class_name = class_name
    #     self.grade = grade
    #     self.submitted = False
