# Generated by Django 3.1.4 on 2020-12-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='origin',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
