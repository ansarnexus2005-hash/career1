from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from carriera.models import *
from carriera.form import *
from carriera.serializers import *

class LoginView(View):
    def get(self,request):
        return render(request, "Administration/login.html")
    def post(self,request):
        username1 = request.POST['Username']
        password1 = request.POST['Password']
        try:
            obj = LoginTable.objects.get(Username=username1, Password=password1)
            request.session['userid'] = obj.id
            # Handle based on user type
            if obj.UserType =='admin':
                return HttpResponse('''<script>alert("welcome back");window.location='/AdminHome'</script>''')
            elif obj.UserType =='HR':
                 return HttpResponse('''<script>alert("welcome back");window.location='/Homepagehr'</script>''')
            else:
                return HttpResponse('''<script>alert("user not found");window.location='/'</script>''')
        except LoginTable.DoesNotExist:
            #Handle care where login details does not exit  
                return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')
        

# /////////////////////////////////////////////////Administration ////////////////////////////////////////////////
#    
class Complaint(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        print(obj)
        return render(request, "Administration/complaint.html", {'val': obj}) 
    
class CompReply(View):
    def post(self,request,complaint_id):
        reply = request.POST['Reply']
        obj = ComplaintTable.objects.get(id=complaint_id)
        obj.Reply=reply
        obj.save()
        return HttpResponse('''<script>alert("reply sended successfully");window.location='/Complaint'</script>''')



class Course(View):
    def get(self,request):
        obj = CollegeTable.objects.all()
        return render(request,'Administration/addcourse.html',{'college':obj})
    def post(self,request):
        c=CourseForm(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('added successfully');window.location='/course'</script>''')
class Viewcourse(View):
    def get(self,request):
        course=CourseTable.objects.all()
        return render(request,'Administration/viewcourse.html',{'course':course})
    
class EditCourse(View): 
    def get(self,request, id):
        course = get_object_or_404(CourseTable, id=id)
        print('*****************')
        print(course)
        print('*****************')
        return render(request, 'Administration/editcourse.html',{'course':course})
    def post(self,request, id):

        course = get_object_or_404(CourseTable, id=id)
        course.CourseName = request.POST.get('CourseName') or course.CourseName
        course.duration = request.POST.get('duration') or course.duration
        course.save()
        return HttpResponse('''<script>alert('Updated succesfully');window.location='/Viewcourse'</script>''')   

class Deletecourse(View):
    def get(self,request,id):
        obj=CourseTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert('Deleted Successfully');window.location='/Viewcourse'</script>''')                

   
    
class VerifyHR(View):
    def get(self,request):
        obj = HrRegisterTable.objects.all()
        return render(request, "Administration/VerifyHR.html", {'val':obj})
class ApproveCompany(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        print(obj,'??????????')
        obj.UserType ="HR"
        obj.save()
        return HttpResponse('''<script>alert("Succesfully Approved!");window.location="/VerifyHR";</script>''')
    
class RejectCompany(View):
    def get(self, request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.UserType = "rejected"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Rejected!");window.location="/VerifyHR";</script>''')
    
class Reply(View):
    def get(self,request):
        return render(request, "Administration/reply.html")  
     
class ViewUser(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request, "Administration/viewuser.html",{'val':obj})   
    
class AdminHome(View):
    def get(self,request):
        return render(request, "Administration/homepage.html")
    

    
class Logout(View):
    def get(self,request):
        return HttpResponse('''<script>alert('logout successfully');window.location='/'</script>''')
    


    
# /////////////////////////////////////////////////// HR ///////////////////////////////////////////////////
class Jobrole(View):
    def get(self,request):
        return render(request,'HR/jobrole.html')
    def post(self,request):
        c=JobroleForm(request.POST)
        d=HrRegisterTable.objects.get(loginid__id = request.session['userid'])
        if c.is_valid():
            reg = c.save(commit=False)
            reg.HR_id = d
            reg.save()
            return HttpResponse('''<script>alert('added successfully');window.location='/Viewjobrole'</script>''')


class Register(View):
    def get(self,request):
        return render(request,'HR/register.html',)
    def post(self, request):
        obj = HrRegisterForm(request.POST)
        print(obj)
        if obj.is_valid():
            c = obj.save(commit=False)
            l = LoginTable.objects.create(
                Username=request.POST.get('Username'),
                Password=request.POST.get('Password'),
                UserType='pending'
            )
            c.loginid = l
            c.save()
            return HttpResponse(
                '''<script>alert('Registered successfully');window.location='/'</script>'''
            )
        else:
            # Optional: Log or print form errors for debugging
            print(obj.errors)
            return render(request, 'HR/register.html', {'form': obj})


   
class Viewjobrole(View):
    def get(self,request):
        obj=JobroleTable.objects.all()
        return render(request,"HR/viewjobrole.html",{'val':obj})


    
    
class Viewrequested(View):
    def get(self,request):
        return render(request,'HR/viewrequested.html')
    
class Homepagehr(View):
    def get(self,request):
        return render(request,'HR/homepagehr.html')
    
class Addcollege(View):
    def get(self,request):
        return render(request,'Administration/collegename.html')
    def post(self,request):
        v=CollegeForm(request.POST)
        print("------------------>", request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('''<script>alert('College added successfully');window.location='/ViewCollege'</script>''')
        
class DeleteCollege(View):
    def get(self,request, c_id):
        obj = CollegeTable.objects.get(id=c_id)
        obj.delete()
        return redirect('ViewCollege')
    
class EditCollege(View):
    def get(self,request, c_id):
        obj = CollegeTable.objects.get(id=c_id)
        return render(request,'Administration/Editcollege.html',{'val': obj})
    def post(self,request, c_id):
        obj = CollegeTable.objects.get(id=c_id)
        v=CollegeForm(request.POST, instance=obj)
        print("------------------>", request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('''<script>alert('Edited successfully');window.location='/ViewCollege'</script>''')

    
class ViewCollege(View):
    def get(self,request):
        obj = CollegeTable.objects.all()
        return render(request,'Administration/viewcollege.html',{'val': obj})
    
class Editjobrole(View):
    def get(self,request,c_id):
        obj = JobroleTable.objects.get(id=c_id)
        return render(request,'HR/Editjobrole.html',{'val': obj})
    def post(self,request, c_id):
        obj = JobroleTable.objects.get(id=c_id)
        v=JobroleForm(request.POST, instance=obj)
        print("-------------------->",request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('''<script>alert('Edited successfully');window.location='/Viewjobrole'</script>''')


class Deletejobrole(View):
    def get(self,request, c_id):
        obj = JobroleTable.objects.get(id=c_id)
        obj.delete()
        return redirect('Viewjobrole')
    


# //////////////////////////////////////// API ///////////////////////////////

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class LoginPage(APIView):
    def post(self,request):
        response_dict={}
        username = request.data.get("username")
        password = request.data.get("password")

        print("username received:",username)

        if not username or not password:
            response_dict["message"] = "username and passord required"
            return Response(response_dict,status=status.HTTp_400_BAD_REQUEST)

        t_user = LoginTable.objects.filter(username=username).first()
        print("user object:",t_user)

        if not t_user:
            response_dict["message"] = "user not found"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        
        if t_user.Password != password:
            response_dict["message"] =  "invalid password"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict,status=status.HTTP_200_OK)    

class uploadcertificateApi(APIView):
    def get(self,request):
        try:
            uplodcertificateApi=CertificateTable.objects.all()

            if not uplodcertificateApi.exists():
                return Response([],status.HTTP_200_OK)
            
            serializer=CertificateSerializer(Complaint,many=True)
            return Response(serializer.data,status=status.HTTP_200_ok)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserRequestApi(APIView):
    def post(self,request):
        print("#####################",request.data)
        user_serial = User_Serializer(data=request.data)
        login_serial = Login_Serializer(data=request.data)


        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(UserType='USER')

            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data,status=status.HTTP_201_CREATED)
        
        return Response({
           'login_error':login_serial.errors if not login_valid else None,
           'user_error':user_serial.errors if not data_valid else None 
        },status=status.HTTP_400_BAD_REQUEST)



        





        

        



























