from django.urls import path

from carriera.views import *

urlpatterns = [
    path('',LoginView.as_view(),name='LoginPage'),
    # ///////////////////////////////// ADMIN //////////////////////////////////////////

    path('Complaint',Complaint.as_view(),name='Complaint'),
    path('CompReply/<int:complaint_id>',CompReply.as_view(),name='CompReply'),
    path('VerifyHR',VerifyHR.as_view(),name='VerifyHR'),
    path('ApproveCompany/<int:login_id>/',ApproveCompany.as_view(), name='ApproveCompany'),
    path('RejectCompany/<int:login_id>/',RejectCompany.as_view(),name='RejectCompany'),
    path('ViewUser',ViewUser.as_view(),name='ViewUser'),
    path('Reply',Reply.as_view(),name='Reply'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
    path('course',Course.as_view(),name='course'),
    path('Viewcourse',Viewcourse.as_view(),name='Viewcourse'),
    path('EditCourse/<int:id>/',EditCourse.as_view(),name='EditCourse'),
    path('Deletecourse/<int:id>/',Deletecourse.as_view(),name='Deletecourse'),
    path('logout',Logout.as_view(),name='logout'),
    path('DeleteUser/<int:id>/',DeleteUser.as_view(),name='DeleteUser'),
    
    # ///////////////////////////////// HR /////////////////////////////////////////////
    path('Jobrole',Jobrole.as_view(),name='Jobrole'),
    path('Register',Register.as_view(),name='Register'),
    path('Viewjobrole',Viewjobrole.as_view(),name='Viewjobrole'),
    path('Viewrequested',Viewrequested.as_view(),name='Viewrequested'),
    path('view_resume/<int:id>/',view_resume.as_view(), name='view_resume'),
    path('Homepagehr',Homepagehr.as_view(),name='Homepagehr'),
    path('Addcollege',Addcollege.as_view(),name='Addcollege'),
    path('DeleteCollege/<int:c_id>',DeleteCollege.as_view(),name='DeleteCollege'),
    path('EditCollege/<int:c_id>',EditCollege.as_view(),name='EditCollege'),
    path('ViewCollege',ViewCollege.as_view(),name='ViewCollege'),
    path('Editjobrole/<int:c_id>',Editjobrole.as_view(),name='Editjobrole'),
    path('Deletejobrole/<int:c_id>',Deletejobrole.as_view(),name='Deletejobrole'),







    # ////////////////////////////////////////// API USER /////////////////////////////////////////
    path('user/loginpageapi',LoginPage.as_view(),name='loginpageapi'),
    path('uploadcertificate/api/',uploadcertificateApi.as_view(),name='uploadcertificateapi'),
    path('UserRequest/api/',UserRequestApi.as_view(),name='UserRequestapi'),
    path('viewprofile/api/<int:id>/', viewprofileApi.as_view(), name='viewprofileApi'),


    ]
