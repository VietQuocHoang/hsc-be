# Generated by Django 2.1.4 on 2019-01-03 00:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190103_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsubscriber',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventsubscriber',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='event',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='events.Event'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('O', 'Okay'), ('C', 'Cancelled')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
        migrations.DeleteModel(
            name='EventSubscriber',
        ),
    ]
