from django.forms import ModelForm

from carriera.models import *


class CertificateForm(ModelForm):
    class Meta:
        Model=CertificateTable
        fields=['Name','Certificate','Description','Date','USER']

class ResumeForm(ModelForm):
    class Meta:
        Model=ResumeTable
        fields=['Resume','Date','USER']

class HRForm(ModelForm):
    class Meta:
        Model=HRTable
        fields=['Name','Company_Name','Email','Phone_Number']

class JobroleForm(ModelForm):
    class Meta:
        Model=JobroleTable
        fields=['Title','Description','Experience','Job_Role','Company_Name','Salary']    

class UserRequestForm(ModelForm):
    class Meta:
        Model=UserRequestTable
        fields=['Username','DOB','Email','Qualification','Address','Area_of_Interest','PhoneNo']

class HrRegisterForm(ModelForm):
    class Meta:
        Model=HrRegisterTable
        fields=['Name','CompanyId','Email','Address','PhoneNo']

class RequestForm(ModelForm):
    class Meta:
        Model=RequestTable
        fields=['USER','Status','JOB']

class CourseForm(ModelForm):
    class Meta:
        Model=CourseTable
        fields=['CourseName','Fees','Duration','Vedio']

class ComplaintForm(ModelForm):
    class Meta:
        Model=ComplaintTable
        fields=['Complaint','Reply','Created_at','USER']
        
class CollegeForm(ModelForm):
    class Meta:
        model =CollegeTable
        fields=['collegeName','Address','Email','PhoneNo']
                                 


        