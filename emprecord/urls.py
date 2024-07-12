"""
URL configuration for emprecord project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('employee.urls')),
    path('', index, name='index'),
    path('register/',register, name='register'),
    path('emp_login/',emp_login, name='emp_login'),
    path('emp_home/',emp_home, name='emp_home'),
    path('profile/',profile,name="profile"),
    path('logout_view/',logout_view, name='logout_view'),
    path('admin_login/',admin_login, name='admin_login'),
    path('myexperience/',myexperience, name='myexperience'),
    path('editexperience/',editexperience, name='editexperience'),
    path('education/',education, name='education'),
    path('edit_education/',edit_education, name='edit_education'),
    path('change_password/',change_password, name='change_password'),
    path('admin_login/',admin_login, name='admin_login'),
    path('admin_home/',admin_home, name='admin_home'),
    path('changeadmin_password/',changeadmin_password, name="changeadmin_password"),
    path('all_employee/',all_employee, name='all_employee'),
    path('aedit_education/<int:pid>',aedit_education, name='aedit_education'),
    path('delete_employee/<int:id>',delete_employee, name='delete_employee'),
    path('edit_profile/<int:id>',edit_profile, name='edit_profile'),





]
 