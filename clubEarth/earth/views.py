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

    if request.method == "POST" and "create_event" in request.POST:
        new_event = Event.objects.create(name="Untitled Event", 
                                         host=request.user.profile, 
                                         description="Description of your event.",
                                         location1="101 Example St.",
                                         location2="West Henrietta, NY 14586")
        new_event.save()

        attender = Attending.objects.create(event=new_event, person=request.user.profile)

        return redirect("earth:event_info", event_id=new_event.id)

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
    my_user = request.user.profile

    attendees = Attending.objects.filter(event__id=event.id)
    attendee_count = attendees.count

    context = {
        'event': event,
        'header': "Events_All",
        'my_user': my_user,
        'attendees': attendees,
        'attendee_count': attendee_count
    }

    if request.user.is_authenticated():
        if request.method == 'POST' and 'submit_event_edit' in request.POST:
            eventform = EditEventForm( request.POST )

            if eventform.is_valid():
                event_name = eventform.cleaned_data['name']
                event_description = eventform.cleaned_data['description']
                event_location1 = eventform.cleaned_data['location1']
                event_location2 = eventform.cleaned_data['location2']

                event.name = event_name
                event.description = event_description
                event.location1 = event_location1
                event.location2 = event_location2
                event.save()

                return redirect("earth:event_info", event_id=event.id)
        elif request.method == 'POST' and 'cancel_event_edit' in request.POST:
            return redirect("earth:event_info", event_id=event.id)

        if event.host == my_user:
            eventform = EditEventForm()
            context['event_form'] = eventform

    return render(request, "event_info.html", context)
