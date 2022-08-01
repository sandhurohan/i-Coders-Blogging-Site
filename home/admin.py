from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = "iCoder Admin"
admin.site.site_title = "iCoder Admin Panel"
admin.site.index_title = "Welcome to iCoder Admin Panel"