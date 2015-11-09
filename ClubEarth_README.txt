ClubEarth README

Application requirements:
-python 3.4
-Django 1.8.5

Running the application:
-unzip the 'ClubEarth' zip file
-in a terminal, navigate to the directory where 'manage.py' is located
-run 'python manage.py runserver'
-go to 'localhost:8000' in a browser

Example users: [username : password]

admin : admin
kevin : kevin
ben : ben

======================================

First logged out page:
-at the logged out page, a user may register a new user
-after registering a new user, they may login in at the top right

Logged in home page:
-after logging in, a user is redirected to the home news page
-news articles are listed which will take the user to an external site
-on the left hand side there are links to top threads and events
-the navigation bar on the top of the page will take the user to different pages

Events page:
-users come here by clicking "Events" in the top navigation bar
-events are listed here 
-clicking on an event title will take the user to the event info page
-a user may also click the 'Create Event' link to create an event

Event info page:
-when an event is clicked, the user is taken to this page
-if the user is the host, they may edit the event
-if the user is not the host, they may choose to attend the event
-users may input comments and questions at the bottom of the event info

Forums page:
-users come here by clicking "Forums" in the top navigation bar
-a list of thread categories is listed
-clicking on a category will take the user to a list of threads in that category
-at that page, a user may create a new thread or click to view an existing one and write a comment


=====================================


KNOWN BUGS/ISSUES:
-A user may "attend" an event multiple times by clicking 'Attend This Event' multiple times
-Dates are not showing correctly on the events list page
-The left portion of the events list page does not have real functionality
