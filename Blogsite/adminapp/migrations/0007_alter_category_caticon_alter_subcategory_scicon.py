# Generated by Django 4.0.3 on 2022-05-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_remove_regadmin_id_alter_regadmin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='caticon',
            field=models.ImageField(default='', upload_to='adminapp/images'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='scicon',
            field=models.ImageField(default='', upload_to='adminapp/images'),
        ),
    ]
