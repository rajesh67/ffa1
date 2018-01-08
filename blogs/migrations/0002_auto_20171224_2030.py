# Generated by Django 2.0 on 2017-12-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='image.png', upload_to='uploads/blogs'),
        ),
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default='nothing', max_length=250),
        ),
    ]
