# Generated by Django 3.0.8 on 2020-08-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200721_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
