# Generated by Django 4.0.3 on 2022-05-09 12:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_category_regdate'),
        ('userapp', '0009_delete_addblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.subcategory')),
                ('unm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]