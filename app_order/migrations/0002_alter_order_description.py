# Generated by Django 4.0.2 on 2022-02-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(default='Order description.', max_length=1000),
        ),
    ]
