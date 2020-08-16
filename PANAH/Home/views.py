from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import EndUser, Schema, Employee, Volunteer
from django.contrib.auth.forms import AuthenticationForm
from geopy.geocoders import Nominatim
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def login(request):
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/home.html', {'form': AuthenticationForm(), 'error': "Invalid username or password"})
        else:
            login(request, user)
            try:
                admin = User.objects.filter(username='admin')
                if admin is None:
                    employee = Employee.objects.filter(User=request.user)
                    if employee is None:
                        volunteer = Volunteer.objects.filter(User=request.user)
                        if volunteer is None:
                            use = EndUser.objects.filter(User=request.user)
                            return redirect("viewfilterform")
                        else:
                            return redirect("volunteer")
                    else:
                        return redirect("employee")
                else:
                    return redirect("adminx")
            except Exception as e:
                return render(request, 'home/home.html', {'main_error': 'something went wrong'})
def adminx(request):
    schemes = Schema.objects.all()
    return render(request, 'home/admin.html', {'schemes': schemes})
def employee(request):
    return render(request, 'home/employee.html')
def volunteer(request):
    return render(request, 'home/volunteer.html')
def enduser(request):
    return redirect("viewfilterform")
def schemaview(request, id):
    schemes = Schema.objects.filter(id=id)
    return render(request, "home/schemeview.html", {'schemes': schemes})


def schemaedit(request, id):
    schemes = Schema.objects.filter(id=id)
    return render(request, 'home/schemaedit.html', {'schemes': schemes})


def schemadelete(request, id):
    schemes = Schema.objects.filter(id=id)
    schemes.delete()
    return render(request, 'home/admin.html', {"scheme": scheme})


def viewfilterform(request):
    if request.method == "GET":
        return render(request, 'home/filterform.html')
    else:
        '''
        filtering to be done to the schemes specified
        schemes =
        '''
        return render(request, 'home/filter.html')#sedn the schemes

def signupemp(request):
    if request.method == "GET":
        return render(request, 'home/signupEmp.html')
    else:
        try:
            username = request.POST['username']
            full_Name = request.POST['full_Name']
            email = request.POST['email']
            ngo_id = request.POST['ngo_id']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            location = request.POST['location']
            if password1 == password2:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                Employee.objects.create(
                    user=user, full_Name=user_no, email=email, ngo_id=ngo_id, location=location)
                return render(request, 'home/employee.html')
            else:
                return render(request, 'home/signupEmp.html', {'error': "Passwords don't match'"})
        except Exception as e:
            print(e)
            return render(request, 'home/signupEmp.html', {'error': "Invalid entry of data"})
def signupVol(request):
    if request.method == "GET":
        return render(request, 'home/signupVol.html')
    else:
        try:
            username = request.POST['username']
            phone_number = request.POST['phone_number']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            location = request.POST['location']
            if password1 == password2:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                Volunteer.objects.create(
                    user=user, phone_number=phone_number, location=location)
                return render(request, 'home/volunteer.html')
            else:
                return render(request, 'home/signupEmp.html', {'error': "Passwords don't match'"})
        except Exception as e:
            print(e)
            return render(request, 'home/signupEmp.html', {'error': "Invalid entry of data"})
def logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect("home")
