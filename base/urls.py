from django.urls import path 

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login_view,name="login"),
    path("verifyNumber/",views.verifyNumber,name="verifyNumber"),
    path("verify/<str:phone_no>/",views.verify,name="verify"),
]