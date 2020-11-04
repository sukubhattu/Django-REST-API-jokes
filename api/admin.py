from django.contrib import admin

# import models
from .models import Jokes

# Register your models here
admin.site.register(Jokes)
