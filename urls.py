
from django.contrib import admin
from django.urls import path
from student_registration import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',views.show),
]
