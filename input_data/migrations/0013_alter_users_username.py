# Generated by Django 4.1.5 on 2023-01-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0012_invnum_netname_alter_invnum_brand_alter_invnum_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='UserName',
            field=models.CharField(max_length=100),
        ),
    ]