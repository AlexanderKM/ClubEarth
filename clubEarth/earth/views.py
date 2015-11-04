from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from earth.models import *
from earth.forms import *

# Create your views here.
def index(request):

    if request.user.is_authenticated():
        return redirect("earth:home")

    if request.method == "POST":
        if "email" in request.POST:
            user_form = UserForm(request.POST)
            profile_form = ProfileForm(request.POST)

            if user_form.is_valid():
                django_user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = django_user
                profile.save()

                profile_form = ProfileForm()
                user_form = UserForm()

                context = {
                    "user_form": user_form,
                    "profile_form":profile_form,
                    "register_success": True,
                }

                return render(request, "index.html", context)


    user_form = UserForm()
    profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, "index.html", context)

def home(request):

    return render(request, "home.html")


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
        return redirect("earth:index")
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
        'categories': Category.objects.all(),
        'header': "Forums_All",
    }
    return render(request, "forums.html", context)

def forum_category(request, category_id=0):
    category = get_object_or_404(Category, pk=category_id)
    threads = Thread.objects.filter(category=category)

    context = {
        'category': category,
        'threads': threads,
        'header': "Forums_All",
    }

    return render(request, "forum_category.html", context)

def thread_info(request, thread_id=0):
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = Comment.objects.filter(thread=thread)

    context = {
        'thread': thread,
        'comments': comments,
        'header': "Forums_All",
    }

    return render(request, "thread_info.html", context)

def event_info(request, event_id=0):
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
        'header': "Events_All",
    }
    return render(request, "event_info.html", context)
