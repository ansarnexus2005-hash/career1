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



class JobroleForm(ModelForm):
    class Meta:
        model=JobroleTable
        fields=['category','Description','Experience','Job_Role','Salary']    


class HrRegisterForm(ModelForm):
    class Meta:
        model=HrRegisterTable
        fields=['Name','Email','Address','PhoneNo']

class RequestForm(ModelForm):
    class Meta:
        model=RequestTable
        fields=['USER','Status','JOB']

class CourseForm(ModelForm):
    class Meta:
        model=CourseTable
        fields=['CourseName','college','duration']

class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Complaint','Reply','USER']
        
class CollegeForm(ModelForm):
    class Meta:
        model =CollegeTable
        fields=['collegeName','Address','Email','PhoneNo','weblink']
                                 


        