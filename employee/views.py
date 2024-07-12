from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    error =""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pw = request.POST['password']

        # exp = EmployeeExperience.objects.all()

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pw)
            EmployeeDetail.objects.create(user = user, empcode=ec)
            EmployeeExperience.objects.create(user = user )
            EmployeeEducation.objects.create(user = user)

            error = "no"
        except:
            error = "yes"
        
    return render(request, 'register.html', locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    
    return render(request, 'emp_login.html',locals())


def emp_home(request):
    # if not request.user.is_authenticated():
    #     return redirect('emp-login')
    return render(request, 'emp_home.html')


def profile(request):
    
    error =""
    user = request.user   # to get current user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        des = request.POST['designation']
        dept = request.POST['department']
        contact = request.POST['contact']
        jd = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.designation = des
        employee.emdept = dept
        employee.contact = contact
        employee.joiningdate = jd
        employee.gender = gender

        if jd:
            employee.joiningdate = jd

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"
        
    return render(request, 'profile.html', locals())


def logout_view(request):
    logout(request)
    return redirect('index')

def admin_login(request):
    return render(request, 'admin_login.html')

def myexperience(request):
    # if not request.user.is_authenticated():
    #    return redirect('emp_login')

    user = request.user
    emp_exp = EmployeeExperience.objects.get(user=user)
    return render(request, 'myexperience.html',locals())


def editexperience(request):
    error =""
    user = request.user   # to get current user
    emp_exp = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        emp_exp.company1name = company1name
        emp_exp.company1desig = company1desig
        emp_exp.company1salary = company1salary
        emp_exp.company1duration = company1duration
        
        emp_exp.company2name = company2name
        emp_exp.company2desig = company2desig
        emp_exp.company2salary = company2salary
        emp_exp.company2duration = company2duration

        emp_exp.company3name = company3name
        emp_exp.company3desig = company3desig
        emp_exp.company3salary = company3salary
        emp_exp.company3duration = company3duration


        try:
            emp_exp.save()
            # emp_exp.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editexperience.html',locals())


def education(request):
    # if not request.user.is_authenticated():
    #    return redirect('emp-login')

    user = request.user
    edu = EmployeeEducation.objects.get(user=user)
    return render(request, 'education.html',locals())


def edit_education(request):
    error =""
    user = request.user   # to get current user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        pgcourse = request.POST['pgcourse']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']

        gracourse = request.POST['gracourse']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        ssccourse = request.POST['ssccourse']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        hsccourse = request.POST['hsccourse']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']


        education.pgcourse = pgcourse
        education.schoolclgpg = schoolclgpg
        education.yearofpassing = yearofpassing
        education.percentagepg = percentagepg
        
        education.gracourse = gracourse
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.ssccourse = ssccourse
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.hsccourse = hsccourse
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc


        try:
            education.save()
            # emp_exp.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_education.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error =""
    user = request.user   # to get current user
    
    if request.method == 'POST':
        c= request.POST['current_pass']
        n= request.POST['new_pass']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_password.html',locals())


def admin_login(request):

    # if not request.user.is_authenticated():
    #      return redirect('admin_login')

    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    
    return render(request, 'admin_login.html',locals())


def admin_home(request):
    # if not request.user.is_authenticated():
    #      return redirect('admin_login')
    return render(request, 'admin_home.html')


def changeadmin_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error =""
    user = request.user   # to get current user
    
    if request.method == 'POST':
        c= request.POST['current_pass']
        n= request.POST['new_pass']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'changeadmin_password.html',locals())


def all_employee(request):
    # if not request.user.is_authenticated():
    #      return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html',locals())



def aedit_education(request,pid):
    error =""
    user = request.user   # to get current user
    user = User.objects.get(id=pid)
    # education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        pgcourse = request.POST['pgcourse']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']

        gracourse = request.POST['gracourse']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        ssccourse = request.POST['ssccourse']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        hsccourse = request.POST['hsccourse']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']


        education.pgcourse = pgcourse
        education.schoolclgpg = schoolclgpg
        education.yearofpassing = yearofpassing
        education.percentagepg = percentagepg
        
        education.gracourse = gracourse
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.ssccourse = ssccourse
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.hsccourse = hsccourse
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc


        try:
            education.save()
            # emp_exp.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'aedit_education.html',locals())


def delete_employee(request,id):
    user = request.user
    emp_delete = EmployeeDetail.objects.get(id=id)
    emp_delete.delete()
    return redirect('admin_home')


def edit_profile(request,id):
    
    error =""
    user = request.user   # to get current user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        des = request.POST['designation']
        dept = request.POST['department']
        contact = request.POST['contact']
        jd = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.designation = des
        employee.emdept = dept
        employee.contact = contact
        employee.joiningdate = jd
        employee.gender = gender

        if jd:
            employee.joiningdate = jd

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"
        
    return render(request, 'edit_profile.html', locals())

