# Generated by Django 4.0.2 on 2022-02-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_subscription', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubscription',
            name='can_order',
        ),
        migrations.AddField(
            model_name='subscription',
            name='can_order',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='ordered',
            field=models.IntegerField(default=0),
        ),
    ]
