# Generated by Django 4.2.8 on 2023-12-17 06:01
from django.core.management import call_command
from django.db import migrations, models


def add_fixture(apps, schema_editor):  # noqa: C901
    """Добавление fixtures."""
    call_command("loaddata", "g_ena")


class Migration(migrations.Migration):

    dependencies = [
        ('g_mtg', '0002_alter_projectsalechannel_prompt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsalechannel',
            name='prompt',
            field=models.TextField(
                blank=True, verbose_name='Подсказка для генерации продукта'
            ),
        ),
        migrations.RunPython(
            add_fixture,
            migrations.RunPython.noop,
        ),
    ]
