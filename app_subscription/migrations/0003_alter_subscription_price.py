# Generated by Django 4.0.2 on 2022-02-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_subscription', '0002_remove_usersubscription_can_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
