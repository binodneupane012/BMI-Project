# Generated by Django 3.2.2 on 2021-05-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount_app', '0003_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
    ]
