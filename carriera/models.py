from django.db import models
 
class LoginTable(models.Model):
  Username = models.CharField(max_length=100)
  Password= models.CharField(max_length=100)
  UserType = models.CharField(max_length=50, null=True,blank=True)

class UserTable(models.Model):
   Name = models.CharField(max_length=100, null=True, blank=True)
   DOB = models.CharField(max_length=100, null=True, blank=True)
   Email = models.CharField(max_length=100, null=True, blank=True)
   Qualification = models.CharField(max_length=100, null=True, blank=True)
   Area_Of_Interest = models.CharField(max_length=100, null=True, blank=True)
   PhoneNo = models.CharField(max_length=100, null=True, blank=True)
   LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)

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

class HrRegisterTable(models.Model):
   Name = models.CharField(max_length=100,unique=True)
   Email = models.CharField(max_length=100,unique=True)
   Address = models.CharField(max_length=100, null=True, blank=True)
   PhoneNo = models.BigIntegerField(null=True, blank=True)
   loginid= models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)

class CollegeTable(models.Model):
   collegeName= models.CharField(max_length=100,null=True, blank=True)
   Address = models.CharField(max_length=100,null=True, blank=True)
   Email = models.CharField(max_length=50)
   PhoneNo = models.BigIntegerField(null=True, blank=True)
   weblink = models.CharField(max_length=100,null=True,blank=True)

class CourseTable(models.Model):
   CourseName = models.CharField(max_length=100,unique=True)
   college = models.ForeignKey(CollegeTable, on_delete=models.CASCADE)
   duration=models.CharField(max_length=100,null=True,blank=True)
 
class JobroleTable(models.Model):
   category=models.CharField(max_length=100,null=True,blank=True)
   Description = models.CharField(max_length=1000)
   Experience = models.CharField(max_length=100)       
   Job_Role= models.CharField(max_length=100)
   Salary = models.CharField(max_length=50)
   HR_id = models.ForeignKey(HrRegisterTable, on_delete=models.CASCADE,null=True,blank=True)


class RequestTable(models.Model):
   USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
   Status = models.CharField(max_length=100,unique=True) 
   JOB =  models.ForeignKey(JobroleTable, on_delete=models.CASCADE)

   

class ComplaintTable(models.Model):
   Complaint = models.CharField(max_length=1000)
   Reply = models.CharField(max_length=1000,null=True, blank=True)
   Created_at = models.DateField(auto_now_add=True,null=True, blank=True)
   USER =  models.ForeignKey(UserTable, on_delete=models.CASCADE)


 