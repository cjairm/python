# Generated by Django 3.1.4 on 2020-12-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20201202_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='origin',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]