# Generated by Django 3.0.3 on 2020-02-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_icon_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='text',
            field=models.CharField(blank=True, max_length=100, verbose_name='значение'),
        ),
    ]