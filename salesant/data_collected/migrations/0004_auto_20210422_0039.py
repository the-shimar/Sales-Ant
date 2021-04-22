# Generated by Django 3.1.7 on 2021-04-21 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_collected', '0003_auto_20210422_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_new_subscriber',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dc_new_subscriber',
            name='name',
            field=models.CharField(default='BuildUser', max_length=200),
        ),
        migrations.AddField(
            model_name='dc_new_subscriber',
            name='subject',
            field=models.CharField(default='BuildUser', max_length=200),
        ),
    ]
