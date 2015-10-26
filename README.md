# ClubEarth

Requirements:
* python 3.4
* django 1.8.5

## Installing/Updating Django on windows 
Install python 3.4 and git bash (or your terminal of choice).
In a terminal, run `pip install Django==1.8.5`

## First time running the application
* clone repo
* `python manage.py syncdb`
* `python manage.py migrate`
* `python manage.py runserver`

## Migrations
When changes are made to the models, the database needs to be migrated (or destroyed and re-made).
To migrate, run:
`python manage.py makemigrations`
`python manage.py migrate`
