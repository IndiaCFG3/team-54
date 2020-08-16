from django.shortcuts import render,redirect
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


def loginx(request):
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/home.html', {'form': AuthenticationForm(), 'error': "Invalid username or password"})
        else:
            try:
                login(request,user)
                admin = User.objects.filter(username='admin')
                if request.POST['username']!='admin':
                    employee = Employee.objects.filter(user=request.user)
                    if len(employee)==0:
                        volunteer = Volunteer.objects.filter(user=request.user)
                        if len(volunteer)==0:
                            use = EndUser.objects.filter(user=request.user)
                            return render(request,'home/enduser.html')
                        else:
                            return redirect("volunteer")
                    else:
                        return redirect("employee")
                else:
                    return redirect("adminx")
            except Exception as e:
                print(e)
                return render(request, 'home/home.html', {'main_error': 'something went wrong'})
def adminx(request):
    schemes = Schema.objects.all()
    return render(request, 'home/admin.html', {'schemes': schemes})
def employee(request):
    return render(request, 'home/employee.html')
def volunteer(request):
    if request.method == 'POST':
        income = request.POST['income']
        state = request.POST['state']
        fam_size = request.POST['fam_size']
        living = request.POST['living']
        organization = request.POST['organization']
        gender = request.POST['gender']
        Schemes = Schema.objects.all().filter(gender=gender).filter(state=state).filter(living=living).filter(organization=organization).filter(income_min__gte=income).filter(income_max__lte=income)
        print(Schemes)
        return render(request, 'home/volunteer.html',{'Schemes':Schemes})
    else:
        return render(request, 'home/volunteer.html')
def enduser(request):
    return redirect("viewfilterform")
def schemaview(request, id):
    schemes = Schema.objects.filter(id=id)
    return render(request, "home/schemeview.html", {'schemes': schemes})
def schemaadd(request):
    description = request.POST['description']
    title = request.POST['title']
    income_max = request.POST['income_max']
    income_min = request.POST['income_min']
    state = request.POST['state']
    max_fam = request.POST['max_fam']
    min_fam = request.POST['min_fam']
    living = request.POST['living']
    organization = request.POST['organization']
    gender = request.POST['gender']
    Schema.objects.create(title=title, description=description,
    income_max=income_max,income_min=income_min,state=state,
    max_fam=max_fam,min_fam=min_fam,living=living,organization=organization,gender=gender)
    return redirect("adminx")

def schemaedit(request,id):
    if request.method =="GET":
        schemes = Schema.objects.filter(id=id)
        return render(request, 'home/schemaedit.html', {'id': id})
    else:
        description = request.POST['description']
        title = request.POST['title']
        income_max = request.POST['income_max']
        income_min = request.POST['income_min']
        state = request.POST['state']
        max_fam = request.POST['max_fam']
        min_fam = request.POST['min_fam']
        living = request.POST['living']
        organization = request.POST['organization']
        gender = request.POST['gender']
        Schema.objects.filter(id=id).update(title=title, description=description,
        income_max=income_max,income_min=income_min,state=state,
        max_fam=max_fam,min_fam=min_fam,living=living,organization=organization,gender=gender)
        return redirect("schemaview",id)


def schemadelete(request, id):
    schemes = Schema.objects.filter(id=id)
    schemes.delete()
    return redirect("adminx")


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
                userx = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                userx.save()
                Employee.objects.create(
                    user=userx, full_Name=full_Name, email=email, ngo_id=ngo_id, location=location)
                return redirect("adminx")
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
                return redirect("employee")
            else:
                return render(request, 'home/signupEmp.html', {'error': "Passwords don't match'"})
        except Exception as e:
            print(e)
            return render(request, 'home/signupEmp.html', {'error': "Invalid entry of data"})
def logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect("home")
