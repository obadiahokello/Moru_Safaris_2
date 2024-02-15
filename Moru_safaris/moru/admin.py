from django.contrib import admin
from .models import service, team, tour, footer

# Register your models here.
admin.site.register(service)
admin.site.register(team)
admin.site.register(tour)
admin.site.register(footer)