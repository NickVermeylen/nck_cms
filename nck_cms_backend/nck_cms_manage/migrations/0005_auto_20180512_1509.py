# Generated by Django 2.0.5 on 2018-05-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nck_cms_manage', '0004_auto_20180512_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_description',
            field=models.TextField(null=True),
        ),
    ]
