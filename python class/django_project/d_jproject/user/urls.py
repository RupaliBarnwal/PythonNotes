from django.urls import path
from . import views

urlpatterns = [
    path("",views.index), #"" --> localhost/user, domain/user
    path("home/",views.home), # localhost/user/home --> home function
     path("index/",views.myhome), #localhost/user/index --> myhome
    path("login/",views.login),
    path("afterlogin/",views.afterlogin),
    path("signup/",views.signup)
]