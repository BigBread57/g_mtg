# Generated by Django 4.2.8 on 2023-12-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_mtg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsalechannel',
            name='prompt',
            field=models.CharField(
                blank=True,
                max_length=1000,
                verbose_name='Подсказка для генерации продукта',
            ),
        ),
    ]