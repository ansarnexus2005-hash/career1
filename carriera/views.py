from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from carriera.models import *
from carriera.form import CourseForm

class LoginPage(View):
    def get(self,request):
        return render(request, "Administration/login.html")
    def post(self,request):
        username1 = request.POST['Username']
        password1 = request.POST['Password']
        try:
            obj = LoginTable.objects.get(Username=username1, Password=password1)
            request.session['username'] = obj.id
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
    
class Course(View):
    def get(self,request):
        return render(request, "Administration/course.html")
    
    
class VerifyHR(View):
    def get(self,request):
        obj = HRTable.objects.all()
        return render(request, "Administration/verifyHR.html", {'val':obj})
    
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
        return HttpResponse('''<script>alert('logout successfully');window.location='/LoginPage'</script>''')
    
class addcourse(View):
    def get(self,request):
        return render(request,"Administration/addcourse.html")
    def post(self,request):
        c=CourseForm(request.POST, request.FILES)
        if c.is_valid():
            c.save()
        return HttpResponse('''<script>alert('logout successfully');window.location='/LoginPage'</script>''')


    
# /////////////////////////////////////////////////// HR ///////////////////////////////////////////////////
class Jobrole(View):
    def get(self,request):
        return render(request,'HR/jobrole.html')

class Register(View):
    def get(self,request):
        return render(request,'HR/register.html')

   
class Viewjobrole(View):
    def get(self,request):
        return render(request,'HR/viewjobrole.html')
    
class Viewrequested(View):
    def get(self,request):
        return render(request,'HR/viewrequested.html')
    
class Homepagehr(View):
    def get(self,request):
        return render(request,'HR/homepagehr.html')





        

        



























