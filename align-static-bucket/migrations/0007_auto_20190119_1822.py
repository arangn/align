# Generated by Django 2.1.5 on 2019-01-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('align', '0006_sequence_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pose',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]