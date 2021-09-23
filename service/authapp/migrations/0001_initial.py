# Generated by Django 3.2.7 on 2021-09-23 20:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.UUID('de6107f5-9b1f-4d4b-b084-2520e6de6171'), primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('token', models.CharField(blank=True, max_length=64)),
            ],
        ),
    ]