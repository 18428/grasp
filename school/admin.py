from django.contrib import admin

# Register your models here.
from school.models import Menu, User

admin.site.register(Menu)
admin.site.register(User)
