# Generated by Django 3.1.7 on 2021-03-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0002_auto_20210323_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertriggers',
            name='user',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
