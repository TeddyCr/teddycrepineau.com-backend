# Generated by Django 2.1.4 on 2019-01-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190101_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelTable(
            name='posts',
            table='posts',
        ),
    ]