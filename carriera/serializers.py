from rest_framework.serializers import ModelSerializer
from carriera.models import *

class CertificateSerializer(ModelSerializer):
    class Meta:
        model=CertificateTable
        fields=['Name','Certificate','Description','Date','USER']

class Resumeserializer(ModelSerializer):
    class Meta:
        model=ResumeTable
        fields=['Resume','Date','USER']       
    
class Jobroleserializer(ModelSerializer):
    class Meta:
        model=JobroleTable
        fields=['Title','Description','Experience','Job_Role','Salary']    


class UserRequestserializer(ModelSerializer):
    class Meta:
        model=UserRequestTable
        fields=['Username','DOB','Email','Qualification','Address','Area_of_Interest','PhoneNo']

class HrRegisterserializer(ModelSerializer):
    class Meta:
        model=HrRegisterTable
        fields=['Name','CompanyId','Email','Address','PhoneNo']

class Requestserializer(ModelSerializer):
    class Meta:
        model=RequestTable
        fields=['USER','Status','JOB']

class Courseserializer(ModelSerializer):
    class Meta:
        model=CourseTable
        fields=['CourseName','college']

class Complaintserializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['Complaint','Reply','USER']

class Collegeserializer(ModelSerializer):
    class Meta:
        model =CollegeTable
        fields=['collegeName','Address','Email','PhoneNo']
                                 
class User_Serializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['Name','DOB','Email','Qualification','Area_Of_Interest','PhoneNo']


class Login_Serializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','UserType']