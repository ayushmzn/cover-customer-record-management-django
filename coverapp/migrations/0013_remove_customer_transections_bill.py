# Generated by Django 3.1.1 on 2020-11-19 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0012_customer_transections_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_transections',
            name='bill',
        ),
    ]
