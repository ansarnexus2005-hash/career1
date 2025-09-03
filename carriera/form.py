from django.forms import ModelForm

from carriera.models import *


class CertificateForm(ModelForm):
    class Meta:
        model=CertificateTable
        fields=['Name','Certificate','Description','Date','USER']

class ResumeForm(ModelForm):
    class Meta:
        model=ResumeTable
        fields=['Resume','Date','USER']

class HRForm(ModelForm):
    class Meta:
        model=HRTable
        fields=['Name','Company_Name','Email','Phone_Number']

class JobroleForm(ModelForm):
    class Meta:
        model=JobroleTable
        fields=['Title','Description','Experience','Job_Role','Salary']    

class UserRequestForm(ModelForm):
    class Meta:
        model=UserRequestTable
        fields=['Username','DOB','Email','Qualification','Address','Area_of_Interest','PhoneNo']

class HrRegisterForm(ModelForm):
    class Meta:
        model=HrRegisterTable
        fields=['Name','CompanyId','Email','Address','PhoneNo']

class RequestForm(ModelForm):
    class Meta:
        model=RequestTable
        fields=['USER','Status','JOB']

class CourseForm(ModelForm):
    class Meta:
        model=CourseTable
        fields=['CourseName','Fees','Duration','Video']

class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Complaint','Reply','USER']
        
class CollegeForm(ModelForm):
    class Meta:
        model =CollegeTable
        fields=['collegeName','Address','Email','PhoneNo']
                                 


        