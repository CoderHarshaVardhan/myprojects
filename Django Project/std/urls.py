from django.contrib import admin
from django.urls import include, path
from std import views

urlpatterns = [
    path('',views.a,name='a'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('add/',views.add,name='addData'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('login/',views.login, name='login'),
    path('cse/',views.cse,name='cse'),
    path('cs/',views.cs,name='cs'),
    path('ds/',views.ds,name='ds'),
    path('aiml/',views.aiml,name='aiml'),
    path('logout/',views.logout,name='logout'),
    path('search/', views.search, name="search"),
    path('cse_data/',views.search,name='cse_data'),
    path('cs_data/',views.cs_data_search,name='cs_data'),
    path('ds_data/',views.ds_data_search,name='ds_data'),
]
