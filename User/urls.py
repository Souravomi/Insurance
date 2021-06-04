from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('Logout',views.Logout,name="Logout"),
    path('ChildrensInsurance',views.Life_Children,name="Life_Children"),
    path('EmploysInsurance',views.Life_Employ,name="Life_Employ"),
    path('HealthInsurance',views.Health,name="Health"),
    path('Mypolicies',views.Mypolicy,name="Mypolicy"),
    path('Vehicle',views.Vehicle,name="Vehicle"),
    path('Appliances',views.Appliances,name="Appliances"),
    path('Payment',views.Payment,name="Payment"),
    path('Change_Password',views.Passwordupdate,name='Passwordupdate'),
    path('Download',views.Download,name='Download'),
]