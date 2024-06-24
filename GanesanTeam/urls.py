
from django.urls import path
from . import  views

app_name="physicalclaims"

urlpatterns = [

    path('', views.login,name='login'),
    path('index.html', views.processlogin,name='processlogin'),
    path('home.html',views.home,name='home'),
    path('logout.html',views.logout,name='logout'),
    path('physicalclaimformsubmit.html',views.claimformsubmit,name='claimformsubmit'),

]