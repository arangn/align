# Generated by Django 2.1.5 on 2019-01-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('align', '0004_auto_20190117_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='poses',
        ),
        migrations.AddField(
            model_name='sequence',
            name='poses',
            field=models.ManyToManyField(to='align.Pose'),
        ),
    ]
