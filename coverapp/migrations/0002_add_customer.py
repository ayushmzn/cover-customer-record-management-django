# Generated by Django 3.1.1 on 2020-09-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('shop_name', models.CharField(max_length=100)),
                ('cus_mobile', models.IntegerField()),
                ('address', models.TextField()),
                ('doc', models.DateField()),
            ],
        ),
    ]