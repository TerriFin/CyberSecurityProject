# Generated by Django 3.1.4 on 2020-12-28 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201228_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': [('store.manager', 'Can Manage Items')]},
        ),
    ]
