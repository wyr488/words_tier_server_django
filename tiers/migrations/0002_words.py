# Generated by Django 3.2.6 on 2021-08-31 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=200)),
                ('levels', models.IntegerField(default=0)),
            ],
        ),
    ]
