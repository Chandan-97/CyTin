from django.contrib import admin

# Register your models here.
from .models import Software
from .models import News
from .models import Requestnew

admin.site.register(Software)
admin.site.register(News)
admin.site.register(Requestnew)