# Generated by Django 3.1.1 on 2020-09-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0002_add_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_customer',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
