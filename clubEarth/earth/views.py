from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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

@login_required
def home(request):

    threads = Thread.objects.all()[:3]
    events = Event.objects.all()[:3]
    articles = Article.objects.all()[:6]


    context = {
        "header": "News_All",
        "threads": threads,
        "events": events,
        "articles": articles,
    }
    return render(request, "home.html", context)

def login_page(request):
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
            context = {
                "login_failed": True,
            }
            return render(request, "login.html", context)

    context = {
        "login_failed": False,
    }
    return render(request, "login.html", context)


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
            context = {
                "login_failed": True,
                "user_form": UserForm(),
                "profile_form": ProfileForm(),
            }
            return render(request, "index.html", context)

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
        attender.save()

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
        'categories': Category.objects.all(),
        'header': "Forums_All",
    }
    return render(request, "forums.html", context)

def forum_category(request, category_id=0):
    category = get_object_or_404(Category, pk=category_id)
    threads = Thread.objects.filter(category=category)

    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.category = category
            thread.author = request.user.profile
            thread.save()
            context = {
                'category': category,
                'threads': Thread.objects.filter(category=category),
                'header': "Forums_All",
                'success': True,
                'thread_form': thread_form,

            }

            return render( request, "forum_category.html", context)

    thread_form = ThreadForm()
    context = {
        'category': category,
        'threads': threads,
        'header': "Forums_All",
        'thread_form': thread_form,
    }

    return render(request, "forum_category.html", context)

def thread_info(request, thread_id=0):
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = Comment.objects.filter(thread=thread)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.thread = thread
            comment.author = request.user.profile
            comment.save()
            context = {
                'thread': thread,
                'comments': Comment.objects.filter(thread=thread),
                'header': "Forums_ALL",
                'success': True,
                'comment_form': comment_form,
            }

            return render(request, "thread_info.html", context)

    comment_form = CommentForm()   
    context = {
        'thread': thread,
        'comments': comments,
        'header': "Forums_All",
        'comment_form': comment_form,
    }

    return render(request, "thread_info.html", context)

@login_required
def create_event(request):
    my_user = request.user.profile

    if request.method == "POST":
        create_event_form = EventForm(request.POST)
        event = create_event_form.save(commit=False)
        event.host = my_user
        event.save()

        attender = Attending.objects.create(event=event, person=my_user)
        attender.save()

        attendees = Attending.objects.filter(event__id=event.id)
        attendee_count = attendees.count

        comments = EventComment.objects.filter(event__id=event.id)

        context = {
            'event': event,
            'header': "Events_All",
            'my_user': my_user,
            'attendees': attendees,
            'attendee_count': attendee_count,
            'comments': comments
         }
        return render(request, "event_info.html", context)

    create_event_form = EventForm()
    context = {
        'event_form': create_event_form,
        'my_user': my_user
    }
    return render(request, "create_event.html", context)

@login_required
def event_info(request, event_id=0):
    event = get_object_or_404(Event, pk=event_id)
    my_user = request.user.profile

    attendees = Attending.objects.filter(event__id=event.id)
    attendee_count = attendees.count

    comments = EventComment.objects.filter(event__id=event.id)

    context = {
        'event': event,
        'header': "Events_All",
        'my_user': my_user,
        'attendees': attendees,
        'attendee_count': attendee_count,
        'comments': comments
    }

    if request.user.is_authenticated():
        if request.method == 'POST' and 'submit_event_edit' in request.POST:
            event_name = request.POST['name']
            event_description = request.POST['description']
            event_location1 = request.POST['location1']
            event_location2 = request.POST['location2']
            event_date = request.POST['date']
            event_time = request.POST['time']

            event.name = event_name
            event.description = event_description
            event.location1 = event_location1
            event.location2 = event_location2
            event.date = event_date
            event.time = event_time
            event.save()

            return redirect("earth:event_info", event_id=event.id)
        elif request.method == 'POST' and 'cancel_event_edit' in request.POST:
            return redirect("earth:event_info", event_id=event.id)

        elif request.method == 'POST' and 'attend_event' in request.POST:    
            attender = Attending.objects.create(event=event, person=request.user.profile)
            attender.save()
            
            return redirect("earth:event_info", event_id=event.id)

        elif request.method == 'POST' and 'create_event_comment' in request.POST:
            event_comment = request.POST['comment']

            comment = EventComment.objects.create(event=event, author=request.user.profile, body=event_comment)
            comment.save()


    return render(request, "event_info.html", context)
