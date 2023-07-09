from operator import ge
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from students.models import Student

# Create your views here.
def show_students(request:HttpRequest):
    context = {
        'students': Student.objects.all(),
    }
    return render(request, 'home.html', context)

def student_edit(request:HttpRequest, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.instrument = request.POST.get('instrument')
        student.save()
        return redirect('home')
    return render(request, 'student_edit.html', {'student': student})

def student_create(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        instrument = request.POST.get('instrument')
        student = Student(name=name, age=age, instrument=instrument)
        student.save()
        return redirect('home')
    return render(request, 'student_create.html')


        