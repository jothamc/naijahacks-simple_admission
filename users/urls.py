from django.urls import path, include
from .views import RegisterView,Suggest

app_name = 'user'
urlpatterns = [
    # path("",IndexPage,name="profile"),
    path('register/',RegisterView,name="register"),
    path('',include("django.contrib.auth.urls")),
    path("suggest/",Suggest,name="suggest")
]
