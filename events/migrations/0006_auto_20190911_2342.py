# Generated by Django 2.2.5 on 2019-09-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190910_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='roll_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]