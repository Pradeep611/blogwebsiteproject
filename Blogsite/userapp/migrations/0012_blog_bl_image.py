# Generated by Django 4.0.3 on 2022-05-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bl_image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
