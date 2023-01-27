# Generated by Django 4.1.5 on 2023-01-26 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Position_id',
            new_name='Position',
        ),
        migrations.AddField(
            model_name='users',
            name='Units',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='input_data.units'),
            preserve_default=False,
        ),
    ]
