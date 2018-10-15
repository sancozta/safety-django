from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r"^", include("polls.urls")),
    path("admin/", admin.site.urls),
]
