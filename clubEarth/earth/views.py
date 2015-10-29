from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from earth.models import *
from earth.forms import *

# Create your views here.
def index(request):

    if request.method == "POST":
        if "register" in request.POST:
            username = request.POST.get('username', '')


    user_form = UserForm()
    profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, "index.html", context)


def login(request):

    if request.user.is_authenticated():
        return redirect("earth:index")

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(request.POST.get('next','earth:index'))
        else:
            return render(request, "index.html", {"login_failed": True})

    return render(request, "index.html")

def logout(request):

    if request.user.is_authenticated():
        auth.logout(request)
        return render(request, "index.html")
    else:
        return redirect("earth:index")

def events(request):
    context = {
        'events': Event.objects.all(),
        'header': "Events_All",
    }
    return render(request, "event_list.html", context)

def news(request):
    context = {
        #'news': News.objects.all(),
        'header': "News_All",
    }
    return render(request, "news_list.html", context)

def forums(request):
    context = {
        #'news': News.objects.all(),
        'header': "Forums_All",
    }
    return render(request, "forums.html", context)

def event_info(request, event_id=0):
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
        'header': "Events_All",
    }
    return render(request, "event_info.html", context)
