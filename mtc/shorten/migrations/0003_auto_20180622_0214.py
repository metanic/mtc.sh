# Generated by Django 2.0.5 on 2018-06-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20180622_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedlocation',
            name='identifier',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
