# Generated by Django 4.1.5 on 2023-01-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0010_alter_invnum_brand_alter_invnum_model_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipments',
            old_name='Hardware_id',
            new_name='Hardware',
        ),
        migrations.RenameField(
            model_name='equipments',
            old_name='User_id',
            new_name='User',
        ),
    ]
