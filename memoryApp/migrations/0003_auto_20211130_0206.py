# Generated by Django 2.2 on 2021-11-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoryApp', '0002_auto_20211129_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='dateOfOccurence',
            field=models.DateField(null=True, verbose_name='date of occurence'),
        ),
    ]
