# Generated by Django 3.2 on 2021-09-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
