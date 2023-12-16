# Generated by Django 4.2.8 on 2023-12-16 06:01

from django.db import migrations, models
import django.db.models.deletion
import rules.contrib.models


class Migration(migrations.Migration):

    dependencies = [
        ('g_mtg', '0002_alter_projectuser_project'),
        (
            'user_request',
            '0002_userrequest_unique_client_data_for_project_sale_channel_and_more',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='project_sale_channel',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='users_requests',
                to='g_mtg.projectsalechannel',
                verbose_name='Канал связи проекта',
            ),
        ),
        migrations.CreateModel(
            name='Message',
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
                ('text', models.TextField(verbose_name='Сообщение')),
                (
                    'message_type',
                    models.CharField(
                        choices=[
                            ('user', 'Пользовательское'),
                            ('system', 'Системное'),
                        ],
                        max_length=255,
                        verbose_name='Тип сообщения',
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('ok', 'Данные сформирован хорошо'),
                            ('error', 'Ошибка при формировании данных'),
                            ('revision', 'Доработка сформированных данных'),
                            ('undefined', 'Не определено'),
                        ],
                        default='undefined',
                        max_length=255,
                        verbose_name='Статус сообщения',
                    ),
                ),
                (
                    'user_request',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='messages',
                        to='user_request.userrequest',
                        verbose_name='Запрос пользователя',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='message',
            constraint=models.CheckConstraint(
                check=models.Q(('message_type__in', ['user', 'system'])),
                name='message_message_type_valid',
            ),
        ),
        migrations.AddConstraint(
            model_name='message',
            constraint=models.CheckConstraint(
                check=models.Q(
                    ('status__in', ['ok', 'error', 'revision', 'undefined'])
                ),
                name='message_message_status_valid',
            ),
        ),
    ]