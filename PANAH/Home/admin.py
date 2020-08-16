from django.contrib import admin
from .models import Schema,EndUser,Employee,Volunteer
# Register your models here.
admin.site.register(Schema)
admin.site.register(EndUser)
admin.site.register(Volunteer)
admin.site.register(Employee)