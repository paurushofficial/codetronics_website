# Generated by Django 2.2.5 on 2019-09-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190910_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
