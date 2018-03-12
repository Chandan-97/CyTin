from django.contrib import admin

# Register your models here.
from .models import Software
from .models import News

admin.site.register(Software)
admin.site.register(News)