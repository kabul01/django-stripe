# Generated by Django 4.0.3 on 2023-02-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_item_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='photo',
        ),
        migrations.AlterModelTable(
            name='item',
            table='Products',
        ),
    ]
