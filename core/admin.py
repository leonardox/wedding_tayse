from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Present)
admin.site.register(Category)
admin.site.register(Indication)
