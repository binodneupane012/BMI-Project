from django.contrib import admin
from bmi_app.models import BMIMeasurement, Suggestion

# Register your models here.
@admin.register(BMIMeasurement)
class BMIMeasurementAdmin(admin.ModelAdmin):
    list_display = ("user", "weight", "height", "bmi", "created", "modified")

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("suggestion", "message", )


