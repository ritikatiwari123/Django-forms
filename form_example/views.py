from django.shortcuts import render

from form_example.forms import Student


# Create your views here.

def student_form(request):
    context = {}
    context['form'] = Student()
    return render(request, "index.html", context=context)
