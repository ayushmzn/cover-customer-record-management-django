# Generated by Django 3.1.1 on 2020-11-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0011_auto_20201013_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_transections',
            name='bill',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
