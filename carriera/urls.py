from django.urls import path

from carriera.views import *

urlpatterns = [
    path('',LoginView.as_view(),name='LoginPage'),
    # ///////////////////////////////// ADMIN //////////////////////////////////////////

    path('Complaint',Complaint.as_view(),name='Complaint'),
    path('CompReply/<int:complaint_id>',CompReply.as_view(),name='CompReply'),
    path('VerifyHR',VerifyHR.as_view(),name='VerifyHR'),
    path('ViewUser',ViewUser.as_view(),name='ViewUser'),
    path('Reply',Reply.as_view(),name='Reply'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
    path('course',Course.as_view(),name='course'),
    path('logout',Logout.as_view(),name='logout'),
    # ///////////////////////////////// HR /////////////////////////////////////////////
    path('Jobrole',Jobrole.as_view(),name='Jobrole'),
    path('Register',Register.as_view(),name='Register'),
    path('Viewjobrole',Viewjobrole.as_view(),name='Viewjobrole'),
    path('Viewrequested',Viewrequested.as_view(),name='Viewrequested'),
    path('Homepagehr',Homepagehr.as_view(),name='Homepagehr'),
    path('Addcollege',Addcollege.as_view(),name='Addcollege'),
    path('DeleteCollege/<int:c_id>',DeleteCollege.as_view(),name='DeleteCollege'),
    path('EditCollege/<int:c_id>',EditCollege.as_view(),name='EditCollege'),
    path('ViewCollege',ViewCollege.as_view(),name='ViewCollege'),
    path('Editjobrole/<int:c_id>',Editjobrole.as_view(),name='Editjobrole'),
    path('Deletejobrole/<int:c_id>',Deletejobrole.as_view(),name='Deletejobrole'),







    # ////////////////////////////////////////// API USER /////////////////////////////////////////
    path('login/api/',LoginPage.as_view(),name='loginapi'),
    path('uploadcertificate/api/',uploadcertificateApi.as_view(),name='uploadcertificateapi'),
    path('UserRequest/api/',UserRequestApi.as_view(),name='UserRequestapi'),
    ]
