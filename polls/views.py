from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.template import RequestContext
from django.shortcuts import redirect
import requests
import json

def Login(req):
    return render(req, "polls/login.html")

@require_POST
def LoginUser(req):
    try:
        Url     = "https://safetyflask.herokuapp.com/login"
        Body    = {
            "email":    req.POST["email"],
            "password": req.POST["password"]
        }
        Headers = { 
            "Authorization": "Basic YWRtaW46c2VjcmV0"
        }
        ResponseRequest = requests.post(Url, data=Body, headers=Headers)
        ResponseJson    = json.loads(ResponseRequest.content)
        return redirect("/home")
    except Exception as err:
        return HttpResponse(err)

def Register(req):
    return render(req, "polls/register.html")

@require_POST
def RegisterUser(req):
    try:
        Url     = "https://safetyflask.herokuapp.com/users"
        Body    = {
            "email":    req.POST["email"],
            "password": req.POST["password"],
            "name":     req.POST["name"],
            "arduino":  req.POST["arduino"]
        }
        Headers         = { "Authorization": "Basic YWRtaW46c2VjcmV0" }
        ResponseRequest = requests.post(Url, data=Body, headers=Headers)
        if ResponseRequest.message == "Create User Sucess":
            return redirect("/")
        else:
            return redirect("/register")
    except Exception as err:
        return HttpResponse(err)

def Home(req):
    try:
        id = "1"
        Url     = "https://safetyflask.herokuapp.com/logs/"+id
        Headers = { "Authorization": "Basic YWRtaW46c2VjcmV0" }
        ResponseRequest = requests.get(Url, headers=Headers)
        ResponseJson = json.loads(ResponseRequest.content)
        return render(req, "polls/home.html", {
            "list"  : ResponseJson,
            "id"    : id
        })
    except Exception as err:
        return HttpResponse(err)