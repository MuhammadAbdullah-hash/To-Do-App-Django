# Generated by Django 3.1.4 on 2021-01-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_data',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
