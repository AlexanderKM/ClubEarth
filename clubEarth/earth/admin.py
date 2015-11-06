from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Attending)
admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Comment)