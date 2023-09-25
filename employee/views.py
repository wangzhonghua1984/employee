from cProfile import label
from pyexpat import model
from random import choices
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django import forms
from django.core.exceptions import ValidationError
from django_select2.forms import Select2MultipleWidget
# Create your views here.
def index(request):
    return render(request,"index.html")
## all functions for department##
def dep_list(request):
    dep_objs= models.Departments.objects.all()
    return render(request,"depart_list.html",{
        "dep_objs": dep_objs
    })

class DepModelForm(forms.ModelForm):
    Dep_name = forms.CharField(min_length=5, label="Department Name")
    Dep_intro = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), min_length=10, label="Department Introduction")
    class Meta:
        model = models.Departments
        fields = ["Dep_name","Dep_intro"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for verbose, filed in self.fields.items():
            filed.widget.attrs = {"class" : "form-control"}

def dep_add(request):
    if request.method == "GET":
        dep_form = DepModelForm()
        return render(request,"depart_add.html", {
            "dep_form": dep_form
        })
    
    dep_form = DepModelForm(data=request.POST)
    if dep_form.is_valid():
        dep_form.save()
        return redirect('/employee/depart/list/')
    
    return render(request,"depart_add.html", {
            "dep_form": dep_form
        })
    
      
def dep_del(request, dep_id):
    obj=models.Departments.objects.filter(id=dep_id).delete()
    return redirect('/employee/depart/list/')


def dep_edit(request, dep_id):
    if request.method == "GET":
        obj=models.Departments.objects.filter(id=dep_id).first()
        return render(request, "depart_edit.html",{
            "edit_obj": obj
        })
        
    edit_dep_name = request.POST.get("Dep_name")
    edit_dep_intro = request.POST.get("Dep_intro")
    models.Departments.objects.filter(id=dep_id).update(Dep_name=edit_dep_name, Dep_intro=edit_dep_intro)
    return redirect('/employee/depart/list/')

## all functions for application    
def app_list(request):
    app_objs= models.Applications.objects.all()
    return render(request,"app_list.html",{
        "app_objs": app_objs
    })
    
class AppModelForm(forms.ModelForm):
    App_name = forms.CharField(min_length=2, label="Application Name")     
    App_intro = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), min_length=10,label="Application Introduction")
    
    class Meta:
        model = models.Applications
        fields = ["App_name","App_intro"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for verbose, filed in self.fields.items():
            filed.widget.attrs = {"class" : "form-control"}



def app_add(request):
    if request.method == "GET":
        app_form = AppModelForm()
        return render(request,"app_add.html", {"app_form": app_form})

    app_form = AppModelForm(data=request.POST)
    if app_form.is_valid():
        app_form.save()
        return redirect('/employee/app/list/')
    
    return render(request,"app_add.html", {
        "app_form": app_form
    })

def app_del(request, app_id):
    obj=models.Applications.objects.filter(id=app_id).delete()
    return redirect('/employee/app/list/')


def app_edit(request, app_id):
    if request.method == "GET":
        obj=models.Applications.objects.filter(id=app_id).first()
        return render(request, "app_edit.html",{
            "edit_obj": obj
        })
        
    edit_app_name = request.POST.get("App_name")
    edit_app_intro = request.POST.get("App_intro")
    models.Applications.objects.filter(id=app_id).update(App_name=edit_app_name, App_intro=edit_app_intro)
    return redirect('/employee/app/list/')   

## all functions for role
def role_list(request):
    role_objs= models.Roles.objects.all()
    return render(request,"role_list.html",{
        "role_objs": role_objs
    })
    
class RoleModelForm(forms.ModelForm):
    Role_name = forms.CharField(min_length=2, label="Role Name")     
    Role_intro = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), min_length=10, label="Role Introduction")
    
    class Meta:
        model = models.Roles
        fields = ["Role_name","Role_intro"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for verbose, filed in self.fields.items():
            filed.widget.attrs = {"class" : "form-control"}



def role_add(request):
    if request.method == "GET":
        role_form = RoleModelForm()
        return render(request,"role_add.html", {"role_form": role_form})

    role_form = RoleModelForm(data=request.POST)
    if role_form.is_valid():
        role_form.save()
        return redirect('/employee/role/list/')
    
    return render(request,"role_add.html", {
        "role_form": role_form
    })

def role_del(request, role_id):
    obj=models.Roles.objects.filter(id=role_id).delete()
    return redirect('/employee/role/list/')


def role_edit(request, role_id):
    if request.method == "GET":
        obj=models.Roles.objects.filter(id=role_id).first()
        return render(request, "role_edit.html",{
            "edit_obj": obj
        })
        
    edit_role_name = request.POST.get("Role_name")
    edit_role_intro = request.POST.get("Role_intro")
    models.Roles.objects.filter(id=role_id).update(Role_name=edit_role_name, Role_intro=edit_role_intro)
    return redirect('/employee/role/list/')   


        
## all functions for employee
def emp_list(request):
    emp_objs = models.Employees.objects.all()
    return render(request,"emp_list.html", {
        "emp_objs" : emp_objs
    })
    
class EmpModelForm(forms.ModelForm):
    Emp_name = forms.CharField(min_length=2, label="Employee Name") 
    Emp_dep = forms.ModelChoiceField(queryset=models.Departments.objects.all(), label="Role of Deployment") 
    Emp_role = forms.ModelChoiceField(queryset=models.Roles.objects.all(), label="Role of Employee") 
    Emp_res_apps = forms.ModelMultipleChoiceField(queryset=models.Applications.objects.all(), label = "Responsible Applications",widget= Select2MultipleWidget )
    
    class Meta:
        model = models.Employees
        fields = ["Emp_name","Emp_dep","Emp_role", "Emp_res_apps"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for verbose, filed in self.fields.items():
            filed.widget.attrs = {"class" : "form-control"}



def emp_add(request):
    if request.method == "GET":
        emp_form = EmpModelForm()
        return render(request,"emp_add.html", {"emp_form": emp_form})

    emp_form = EmpModelForm(data=request.POST)
    if emp_form.is_valid():
        emp_form.save()
        return redirect('/employee/emp/list/')
    
    return render(request,"emp_add.html", {
        "emp_form": emp_form
    })

def emp_del(request, emp_id):
    obj=models.Employees.objects.filter(id=emp_id).delete()
    return redirect('/employee/emp/list/')


def emp_edit(request, role_id):
    if request.method == "GET":
        obj=models.Roles.objects.filter(id=role_id).first()
        return render(request, "role_edit.html",{
            "edit_obj": obj
        })
        
    edit_role_name = request.POST.get("Role_name")
    edit_role_intro = request.POST.get("Role_intro")
    models.Roles.objects.filter(id=role_id).update(Role_name=edit_role_name, Role_intro=edit_role_intro)
    return redirect('/employee/role/list/')   
