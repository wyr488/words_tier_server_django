# Generated by Django 3.2.6 on 2021-09-07 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0004_auto_20210907_1052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
