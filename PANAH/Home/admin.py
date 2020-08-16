from django.contrib import admin
from .models import EndUser,Schema,Employee,Volunteer
# Register your models here.
admin.site.register(Schema)
admin.site.register(Employee)
admin.site.register(Volunteer)
admin.site.register(EndUser)