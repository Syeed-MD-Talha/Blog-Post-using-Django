# Generated by Django 5.0.6 on 2024-06-13 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_blogpost_options_alter_blogpost_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogpost',
            table='post_table',
        ),
    ]