# Generated by Django 5.0.6 on 2024-07-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='farm_id',
            field=models.IntegerField(default=1),
        ),
    ]
