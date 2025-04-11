from django.contrib import admin
from .models import Department, Event, News, Follow,DepartmentCoordinator

admin.site.register(Department)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Follow)
admin.site.register(DepartmentCoordinator)
