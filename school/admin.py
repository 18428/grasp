from django.contrib import admin

# Register your models here.
from school.models import Menu, User, GraspModel, GraspField

admin.site.register(Menu)
admin.site.register(User)
admin.site.register(GraspModel)
admin.site.register(GraspField)
