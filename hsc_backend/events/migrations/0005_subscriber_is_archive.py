# Generated by Django 2.1.4 on 2019-01-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190105_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='is_archive',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
