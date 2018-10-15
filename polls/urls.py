from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r"^$",                              views.Login,                    name="login"),
    url(r"^loginuser/$",                    views.LoginUser,                name="loginuser"),
    url(r"^register/$",                     views.Register,                 name="register"),
   	url(r"^registeruser/$",                 views.RegisterUser,             name="registeruser"),
    url(r"^home/$",                         views.Home,                     name="home"),
]