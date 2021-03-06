# Generated by Django 2.0.9 on 2019-03-26 19:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eservice', '0003_auto_20190319_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='EServiceSign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('eservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eservice.EService', verbose_name='Послугу')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Підпис файлу',
                'verbose_name_plural': 'Підпис файлу',
                'db_table': 'eservice_sign',
            },
        ),
    ]
