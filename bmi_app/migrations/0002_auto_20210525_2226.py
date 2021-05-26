# Generated by Django 3.2.2 on 2021-05-25 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bmi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmimeasurement',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bmimeasurement',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bmi_app', to=settings.AUTH_USER_MODEL),
        ),
    ]
