from django.urls import path, include
from . import  views
from .views import import_claims_tracker

app_name="physicalclaims"

urlpatterns = [

path('',views.login,name='login'),
path('home',views.home,name='home'),
path('logout',views.logout,name='logout'),
path('claimformsubmit',views.claimformsubmit,name='claimformsubmit'),
path('processlogin',views.processlogin,name='processlogin'),

path('export-claims-tracker', views.export_claims_tracker, name='export-claims-tracker'),
path('export-claims-status', views.export_claims_status, name='export-claims-status'),

path('edit/<str:id>/', views.edit, name='edit'),
path('upload',views.import_claims_tracker,name='upload'),
path('delete/<str:id>/', views.delete, name='delete'),
path('claimformupdate',views.claimformupdate,name='claimformupdate'),
path('claimqueueview',views.claimqueueview,name='claimqueueview'),
path('import/', views.import_claims_tracker, name='import-claims-tracker'),

]