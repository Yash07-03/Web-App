from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request, 'home.html')

def register(request):
    form= StudForm(request.POST or None)
    return render(request,'register')