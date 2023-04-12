from django.contrib import admin
from .models import Research, Labs, Papers, Projects
# Register your models here.

admin.site.register(Research)
admin.site.register(Labs)
admin.site.register(Papers)
admin.site.register(Projects)