# Generated by Django 3.1.7 on 2021-03-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apikey', '0006_auto_20210324_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='id',
        ),
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.TextField(default='tHSuodAQ9eM87yaP7H1QZYPH'),
        ),
        migrations.AlterField(
            model_name='apikey',
            name='key_name',
            field=models.CharField(default='None', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='website',
            field=models.CharField(default='None', max_length=200, primary_key=True, serialize=False),
        ),
    ]
