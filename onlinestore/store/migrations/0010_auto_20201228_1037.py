# Generated by Django 3.1.4 on 2020-12-28 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201228_0422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': [('manager', 'Can Manage Items')]},
        ),
    ]