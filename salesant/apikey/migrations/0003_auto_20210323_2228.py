# Generated by Django 3.1.7 on 2021-03-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apikey', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(default='jIRVZgogo-EESaQfq3mQ_EN7', max_length=20),
        ),
    ]
