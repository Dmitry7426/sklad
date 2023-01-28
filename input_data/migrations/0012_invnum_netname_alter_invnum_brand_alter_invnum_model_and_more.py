# Generated by Django 4.1.5 on 2023-01-28 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0011_rename_hardware_id_equipments_hardware_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invnum',
            name='netname',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='invnum',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='input_data.brands'),
        ),
        migrations.AlterField(
            model_name='invnum',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='input_data.models'),
        ),
        migrations.AlterField(
            model_name='invnum',
            name='typ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='input_data.typesequipments'),
        ),
    ]