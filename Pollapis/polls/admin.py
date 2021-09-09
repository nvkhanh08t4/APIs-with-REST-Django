from django.contrib import admin
from .models import Poll, Choice, Vote

# Register your models here.
admin.site.register([Poll, Choice, Vote])