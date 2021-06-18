from django.contrib import admin


from .models import Job,Category, employee

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(employee)