# Generated by Django 4.2.8 on 2023-12-15 09:30

import django.db.models.deletion
import rules.contrib.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('g_mtg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Создан'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True, verbose_name='Изменен'),
                ),
                (
                    'client_id',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='ID клиента из сторонних ресурсов',
                    ),
                ),
                (
                    'source_client_info',
                    models.CharField(
                        max_length=255,
                        verbose_name='Источник информации о клиенте',
                    ),
                ),
                (
                    'client_data',
                    models.JSONField(verbose_name='Данные о клиенте'),
                ),
                (
                    'client_data_decoding',
                    models.JSONField(
                        verbose_name='Расшифровка данных о клиенте'
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('ok', 'Ок'),
                            ('error', 'Ошибка'),
                            ('in_progress', 'В процессе'),
                        ],
                        default='in_progress',
                        max_length=255,
                        verbose_name='Статус запроса',
                    ),
                ),
                (
                    'success_type',
                    models.CharField(
                        choices=[
                            ('sold', 'Продано'),
                            ('reflection', 'Обдумывание'),
                            ('interest', 'Заинтересованность'),
                            ('negative_reaction', 'Негативная реакция'),
                            ('positive_reaction', 'Позитивная реакция'),
                            ('undefined', 'Не определено'),
                        ],
                        default='undefined',
                        max_length=255,
                        verbose_name='Тип успеха',
                    ),
                ),
                (
                    'project_sale_channel',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='users_requests',
                        to='g_mtg.projectsalechannel',
                        verbose_name='Канал связи проетка',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='users_requests',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Пользователь',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Запрос пользователя',
                'verbose_name_plural': 'Запросы пользователей',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]