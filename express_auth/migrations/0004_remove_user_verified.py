# Generated by Django 2.2.8 on 2020-03-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('express_auth', '0003_auto_20200325_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
    ]
