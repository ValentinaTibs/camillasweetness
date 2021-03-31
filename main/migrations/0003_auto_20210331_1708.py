# Generated by Django 3.1.3 on 2021-03-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210331_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagina',
            options={'verbose_name': 'Pagina', 'verbose_name_plural': 'Pagine'},
        ),
        migrations.AddField(
            model_name='pagina',
            name='slug',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
