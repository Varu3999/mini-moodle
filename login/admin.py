from django.contrib import admin
from .models import *
admin.site.register(user_type)
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(sc)
admin.site.register(courses)

# Register your models here.
