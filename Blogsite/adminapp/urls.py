from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('categoryadd/',views.categoryadd,name='categoryadd'),
    path('categoryshow/',views.categoryshow,name='categoryshow'),
    path('categoryupdate/<str:c_id>',views.categoryupdate,name='categoryupdate'),
    path('categorydelete/',views.categorydelete,name='categorydelete'),

    path('subcategoryadd/',views.subcategoryadd,name='subcategoryadd'),
    path('subcategoryshow/',views.subcategoryshow,name='subcategoryshow'),
    path('subcategorydel/<str:scat_id>',views.subcategorydel,name='subcategorydel'),
    path('subcategoryupdate/<str:sc_id>',views.subcategoryupdate,name='subcategoryupdate'),

    path('showblogs/',views.showblogs,name='showblogs'),
    path('showcontacts/',views.showcontacts,name='showcontacts'),
    path('showusers/',views.showusers,name='showusers'),
    path('showsingle/<str:slug>',views.showsingle,name='showsingle'),
    path('deleteblog/<str:bl_id>',views.deleteblog,name='deleteblog'),

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogout',views.adminlogout,name='adminlogout'),

    path('search/',views.search,name='search'),
]

