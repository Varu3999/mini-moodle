from django.contrib import admin
from .models import user_type, student, teacher, sc
admin.site.register(user_type)
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(sc)

# Register your models here.
