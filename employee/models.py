from django.db import models

# Create your models here.
class Departments(models.Model):
    Dep_name=models.CharField(verbose_name="dep_name", max_length=16)
    Dep_intro=models.CharField(verbose_name="dep_intro", max_length=256)
    
    def __str__(self):
        return self.Dep_name
    
  
class Roles(models.Model):
    Role_name=models.CharField(verbose_name="role_name",max_length=56)
    Role_intro=models.CharField(verbose_name="role_intro",max_length=256)
    
    def __str__(self):
        return self.Role_name
    
    
class Applications(models.Model):
    App_name=models.CharField(verbose_name="app_name", max_length=16)
    App_intro=models.CharField(verbose_name="app_intro", max_length=256)
    
    def __str__(self):
        return self.App_name
    
    
class Employees(models.Model):
    Emp_name = models.CharField(verbose_name="emp_name", max_length=32)
    Emp_dep = models.ForeignKey(verbose_name="emp_dep",to="Departments",to_field="id", on_delete=models.CASCADE)
    Emp_role = models.ForeignKey(verbose_name="emp_role",to="Roles", to_field="id", on_delete=models.CASCADE)
    Emp_res_apps = models.ManyToManyField(Applications)