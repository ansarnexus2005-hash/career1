from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from carriera.models import *
from carriera.form import CollegeForm, CourseForm, HrRegisterForm, JobroleForm

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
    
class CompReply(View):
    def post(self,request,complaint_id):
        reply = request.POST['Reply']
        obj = ComplaintTable.objects.get(id=complaint_id)
        obj.Reply=reply
        obj.save()
        return HttpResponse('''<script>alert("reply sended successfully");window.location='/Complaint'</script>''')



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
        return HttpResponse('''<script>alert('added successfully');window.location='/AdminHome'</script>''')


    
# /////////////////////////////////////////////////// HR ///////////////////////////////////////////////////
class Jobrole(View):
    def get(self,request):
        return render(request,'HR/jobrole.html')
    def post(self,request):
        c=JobroleForm(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('added successfully');window.location='/Viewjobrole'</script>''')


class Register(View):
    def get(self,request):
        return render(request,'HR/register.html')
    def post(self,request):
        obj=HrRegisterForm(request.POST)
        if obj.is_valid():
            c=obj.save(commit=False)
            l=LoginTable.objects.create(Username=c.Email, Password=request.POST.get('Password'), UserType='HR')
            c.loginid=l
            c.save()
            return HttpResponse('''<script>alert('Rergistered successfully');window.location='/'</script>''')


   
class Viewjobrole(View):
    def get(self,request):
        obj=JobroleTable.objects.all()
        return render(request,"HR/jobrole.html",{'val':obj})


    
    
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
    



        







        





        

        



























