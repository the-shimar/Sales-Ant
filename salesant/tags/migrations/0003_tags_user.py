# Generated by Django 3.1.7 on 2021-04-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20210325_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='user',
            field=models.CharField(default='DummyUser', max_length=200),
        ),
    ]
