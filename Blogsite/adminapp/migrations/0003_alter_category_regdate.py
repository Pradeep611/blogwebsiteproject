# Generated by Django 4.0.3 on 2022-04-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_category_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='regdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]