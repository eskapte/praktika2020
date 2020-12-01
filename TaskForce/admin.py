from django.contrib import admin
from .models import Task, Document, Category, Profile, Application


admin.site.register(Task)
admin.site.register(Document)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Application)