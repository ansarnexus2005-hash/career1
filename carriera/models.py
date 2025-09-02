from django.db import models
 
class LoginTable(models.Model):
  Username = models.CharField(max_length=100)
  Password = models.CharField(max_length=100)
  UserType = models.CharField(max_length=50, null=True,blank=True)

class UserTable(models.Model):
   Name = models.CharField(max_length=100, null=True, blank=True)
   DOB = models.CharField(max_length=100, null=True, blank=True)
   Email = models.CharField(max_length=100, null=True, blank=True)
   Qualification = models.CharField(max_length=100, null=True, blank=True)
   Area_Of_Interest = models.CharField(max_length=100, null=True, blank=True)
   Phone_Number = models.CharField(max_length=100, null=True, blank=True)
   LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)

class CertificateTable(models.Model):
   Name = models.CharField(max_length=100,unique=True)
   Certificate = models.FileField(unique=True)
   Description = models.CharField(max_length=100, null=True, blank=True)
   Date = models.DateField(null=True,blank=True)
   USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)


class ResumeTable(models.Model):
   Resume = models.FileField(null=True, blank=True)
   Date = models.DateField(null=True, blank=True)
   USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)

class HRTable(models.Model):
   Company_Name = models.CharField(max_length=100, null=True, blank=True)
   Email = models.EmailField(unique=True)
   Phone_Number = models.CharField(max_length=15, unique=True)
   type_of_indusrty=models.CharField(max_length=100,unique=True)

class JobroleTable(models.Model):
   Title = models.CharField(max_length=200, unique=True)
   Description=models.CharField(max_length=1000,unique=True)
   Experience = models.CharField(max_length=1000, unique=True)
   Job_Role = models.CharField(max_length=100, unique=True)       
   Company_Name= models.CharField(max_length=100, unique=True)
   Salary = models.CharField(max_length=50, unique=True)

class UserRequestTable(models.Model):
   Username = models.CharField(max_length=100, unique=True)
   DOB = models.CharField(max_length=100, null=True, blank=True)
   Email = models.CharField(max_length=100, null=True, blank=True)
   Qualification = models.CharField(max_length=100, null=True, blank=True)
   Address = models.CharField(max_length=100, null=True, blank=True)
   Area_of_Interest = models.CharField(max_length=100, null=True, blank=True)
   PhoneNo = models.BigIntegerField()

class HrRegisterTable(models.Model):
   Name = models.CharField(max_length=100,unique=True)
   CompanyId = models.CharField(max_length=100,unique=True)
   Email = models.CharField(max_length=100,unique=True)
   Address = models.CharField(max_length=100, null=True, blank=True)
   PhoneNo = models.BigIntegerField(null=True, blank=True)

class RequestTable(models.Model):
   USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
   Status = models.CharField(max_length=100,unique=True) 
   JOB =  models.ForeignKey(JobroleTable, on_delete=models.CASCADE)

class CourseTable(models.Model):
   CourseName = models.CharField(max_length=100,unique=True)
   Fees = models.CharField(max_length=100,unique=True)
   Duration = models.CharField(max_length=100,unique=True)
   Video = models.FileField('coursevideo/',null=True, blank=True)
   

class ComplaintTable(models.Model):
   Complaint = models.CharField(max_length=1000)
   Reply = models.CharField(max_length=1000,null=True, blank=True)
   Created_at = models.DateField(auto_now_add=True,null=True, blank=True)
   USER =  models.ForeignKey(UserTable, on_delete=models.CASCADE)

class CollegeTable(models.Model):
   collegeName = models.CharField(max_length=100,null=True, blank=True)
   Address = models.CharField(max_length=100,null=True, blank=True)
   Email = models.CharField(max_length=50)
   PhoneNo = models.BigIntegerField(null=True, blank=True)
