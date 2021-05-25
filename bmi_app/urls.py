from django.urls import path
from bmi_app.views import bmi_list, bmi_calculate, bmi_edit, bmi_delete, send_report

app_name = "bmi_app"

urlpatterns = [
    path("bmi-list/", bmi_list, name="bmi_list"),
    path("bmi-calculate/", bmi_calculate, name="bmi_calculate"),
    path("bmi-edit/<int:id>/", bmi_edit, name="bmi_edit"),
    path("bmi-delete/<int:id>/", bmi_delete, name="bmi_delete"),
    path("send_report/", send_report, name="send_report"),
]