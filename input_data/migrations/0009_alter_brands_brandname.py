# Generated by Django 4.1.5 on 2023-01-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0008_rename_invnum_equipments_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='BrandName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]