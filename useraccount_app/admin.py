from django.contrib import admin
from useraccount_app.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "address", "contact", "age", "email")