# Generated by Django 3.1.4 on 2020-12-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='./store_images/placeholder.png', upload_to='store_images'),
        ),
    ]
