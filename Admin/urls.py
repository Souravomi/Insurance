from django.urls import path
from . import views

urlpatterns = [
    path('',views.Admin_Home,name="Admin"),
    path('Life',views.Admin_Life,name="Admin_Life"),
    path('General',views.Admin_General,name="Admin_General"),
    path('Health',views.Admin_Health,name="Admin_Health"),
    path('Logout',views.Logout,name="Logout"),
    path('Users',views.Users,name="User"),
    path('Search',views.Search,name="Search"),
    path('Policy',views.Policy,name="Policy"),
    path('Health_Insurance',views.Admin_Health_Insurance,name="Admin_Health_Insurance"),
    path('Life_Children_Application',views.Admin_Life_Children_Application,name="Admin_Life_Children_Application"),
    path('Life_Employee_Application',views.Admin_Life_Employee_Application,name="Admin_Life_Employee_Application"),
    path('Vehicle_Applications',views.Admin_Vehicle_Applications,name="Admin_Vehicle_Applications"),
    path('Appliances_Applications',views.Admin_Appliances_Applications,name="Admin_Appliances_Applications"),
    path('Download_Life',views.Download_Life,name='Download_Life'),
    path('Download_General',views.Download_General,name='Download_General'),
    path('Download_Health',views.Download_Health,name='Download_Health'),
]