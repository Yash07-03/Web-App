from django import forms
class StudForm(forms.Form):
    First_Name = forms.CharField(max_length=30)
    Last_Name = forms.CharField(max_length=30)
    Course = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=30)
