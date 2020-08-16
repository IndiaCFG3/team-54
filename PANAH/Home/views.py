from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import EndUser,Schema,Employee,Volunteer
from django.contrib.auth.forms import AuthenticationForm
from geopy.geocoders import Nominatim
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def login(request):
    if request.method =="POST":
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/home.html', {'form': AuthenticationForm(), 'error': "Invalid username or password"})
        else:
            login(request, user)
            try:
                admin = User.objects.filter(username='admin')
                if admin is None:
                    employee=Employee.objects.filter(User=request.user)
                    if employee is None:
                        volunteer=Volunteer.objects.filter(User=request.user)
                        return render(request,'home/volunteer.html')
                    else:
                        return render(request,'home/employee.html')
                else:
                    schemes = Schema.objects.all()
                    return render(request,'home/admin.html',{'schemes':schemes})
            except Exception as e:
                return render(request,'home/home.html',{'main_error':'something went wrong'})
def schemaview(request,id):
    schemes = Schema.objects.filter(id=id)
    return render(request,"home/schemeview",{'schemes':schemes})
def schemaedit(request,id):
    schemes = Schema.objects.filter(id=id)
    return render(request,'home/schemaedit',{'schemes':schemes})
def schemadelete(request,id):
    schemes = Schema.objects.filter(id=id)
    schemes.delete()
    return render(request,'home/admin.html',{"scheme":scheme})
    