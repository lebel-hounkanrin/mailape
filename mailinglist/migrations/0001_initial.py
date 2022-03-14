# Generated by Django 2.0.13 on 2022-03-04 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('started', models.DateField(default=None, null=True)),
                ('finished', models.DateField(default=None, null=True)),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.MailingList')),
            ],
        ),
        migrations.CreateModel(
            name='Suscriber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('confirmed', models.BooleanField(default=False)),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.MailingList')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='suscriber',
            unique_together={('email', 'mailing_list')},
        ),
    ]