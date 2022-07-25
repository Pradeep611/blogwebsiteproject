from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('reguser',views.reguser,name='reguser'),
    path('registered',views.registered,name='registered'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contactblu/',views.contactblu,name='contactblu'),
    # path('addblogcat/',views.addblogcat,name='addblogcat'),
    path('addblog/',views.addblog,name='addblog'),
    # path('showcatalu',views.showcatalu,name='showcatalu'),
    path('showbloghome/',views.showbloghome,name='showbloghome'),
    path('showblog/<str:slug>',views.showblog,name='showblog'),
    path('myblogs',views.myblogs,name='myblogs'),
    path('updateblog/<str:blg_id>/',views.updateblog,name='updateblog'),
    path('deleteblog/<str:bl_id>/',views.deleteblog,name='deleteblog'),

    path('success/',views.forget_password,name='success'),
    path('search/',views.search,name='search'),
    
]