# Generated by Django 3.1.7 on 2021-03-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0003_usertriggers_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertriggers',
            name='website',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
