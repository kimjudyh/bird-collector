from django.contrib import admin
from .models import Bird, Sighting, NestMaterial

# Register your models here.
admin.site.register(Bird)
admin.site.register(Sighting)
admin.site.register(NestMaterial)
