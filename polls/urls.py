from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r"^$",                              views.Login,                    name="login"),
    url(r"^loginuser/$",                    views.LoginUser,                name="loginuser"),
    url(r"^register/$",                     views.Register,                 name="register"),
   	url(r"^register/registeruser/$",        views.RegisterUser,             name="registeruser"),
    url(r"^update/(?P<id>[0-9]+)$",         views.Update,                   name="update"),
   	url(r"^update/updateuser/$",            views.UpdateUser,               name="updateuser"),
    url(r"^delete/(?P<id>[0-9]+)$",         views.DeleteUser,               name="deleteuser"),
    url(r"^home/(?P<id>[0-9]+)$",           views.Home,                     name="home"),
]