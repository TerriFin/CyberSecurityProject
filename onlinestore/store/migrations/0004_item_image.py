# Generated by Django 3.1.4 on 2020-12-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_item_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='./store/static/store/images/whitehouse2.jpg', upload_to='store_images'),
        ),
    ]
