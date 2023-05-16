from django.shortcuts import render

# Create your views here.
from grade_app.models import Grades
from grade_app.serielizer import GradesSerializer
from grade_app.util import format_serializer_data


def dashboard(request):
    rows_qs = Grades.objects.filter().all()
    rows_s = GradesSerializer(rows_qs, many=True)
    rows_data = format_serializer_data(rows_s.data)
    print('abc')
    print(rows_data, rows_data[0], rows_data[0]["student_name"])
    return render(request, 'dashboard.html', {'rows': rows_data})


def form(request):
    try:
        if request.method == 'POST':
            print(request)
            student_name = request.POST['student_name']
            class_name = request.POST['class_name']
            grade = request.POST['grade']
            marks = request.POST['marks']
            new_entry = Grades(student_name=student_name, class_name=class_name, grade=grade, marks=marks)
            new_entry.save()
            return render(request, 'post_submit.html')
    except Exception as e:
        print(e)
        return render(request,'submit_fail.html')

    return render(request, 'form.html')
