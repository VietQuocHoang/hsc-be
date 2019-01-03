# Generated by Django 2.1.4 on 2019-01-01 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_archive', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_createdby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('O', 'Okay'), ('C', 'Cancelled')], max_length=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_archive', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='host_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='host_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='eventtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.Tag'),
        ),
        migrations.AddField(
            model_name='eventsubscriber',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Subscriber'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Host'),
        ),
        migrations.AddField(
            model_name='event',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers_set', through='events.EventSubscriber', to='events.Subscriber'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='tags_set', through='events.EventTag', to='events.Tag'),
        ),
    ]