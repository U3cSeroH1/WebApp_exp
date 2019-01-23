# Generated by Django 2.1.4 on 2019-01-21 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0007_auto_20190121_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='target',
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
