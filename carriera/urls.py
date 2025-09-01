from django.urls import path

from carriera.views import *

urlpatterns = [
    path('',LoginPage.as_view(),name='LoginPage'),
    # ///////////////////////////////// ADMIN //////////////////////////////////////////

    path('Complaint',Complaint.as_view(),name='Complaint'),
    path('VerifyHR',VerifyHR.as_view(),name='VerifyHR'),
    path('ViewUser',ViewUser.as_view(),name='ViewUser'),
    path('Reply',Reply.as_view(),name='Reply'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
    path('course',Course.as_view(),name='course'),
    path('logout',Logout.as_view(),name='logout'),
    path('addcourse',addcourse.as_view(),name='Addcourse'),
    # ///////////////////////////////// HR /////////////////////////////////////////////
    path('Jobrole',Jobrole.as_view(),name='Jobrole'),
    path('Register',Register.as_view(),name='Register'),
    path('Viewjobrole',Viewjobrole.as_view(),name='Viewjobrole'),
    path('Viewrequested',Viewrequested.as_view(),name='Viewrequested'),
    path('Homepagehr',Homepagehr.as_view(),name='Homepagehr',)
]