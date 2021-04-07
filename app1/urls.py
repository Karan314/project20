from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('<data>/',views.index,name="index"),
    path('sample1/',views.sample,name="sample1"),
    path('temp1/',views.temp1,name="temp1"),
]
