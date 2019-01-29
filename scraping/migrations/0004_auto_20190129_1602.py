# Generated by Django 2.1.4 on 2019-01-29 16:02

from django.db import migrations, models
import django.db.models.deletion
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_auto_20190129_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weatherdetail',
            name='target',
            field=models.ForeignKey(default=scraping.models.get_or_create_date, on_delete=django.db.models.deletion.CASCADE, to='scraping.Date'),
        ),
    ]
