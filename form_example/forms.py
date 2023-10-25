from django import forms


class Student(forms.Form):
    name = forms.CharField(label="enter student name", max_length=100)
    age = forms.IntegerField(label="enter student age")