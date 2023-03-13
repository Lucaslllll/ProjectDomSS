from django.contrib import admin
from .models import Provider, Driver, Notes


admin.site.register(Provider)
admin.site.register(Driver)
admin.site.register(Notes)
