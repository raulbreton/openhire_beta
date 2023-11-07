from django.contrib import admin
from .models import EmployerProfile

class UserAdmin(admin.ModelAdmin):
    model = EmployerProfile
    #Fields to display
    fields = ["user","company_name","description", "location"]

admin.site.register(EmployerProfile, UserAdmin)