# Generated by Django 3.1.7 on 2021-04-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YNF_Form_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='BuildUser', max_length=200)),
                ('trigger_name', models.CharField(default='trigger_name', max_length=200)),
                ('collected_email', models.CharField(default='collected_email', max_length=200)),
            ],
        ),
    ]
