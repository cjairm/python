# Generated by Django 3.1.4 on 2020-12-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20201202_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=50),
        ),
    ]
