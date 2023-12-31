# Generated by Django 4.2.8 on 2023-12-17 11:08

import rules.contrib.models
from django.db import migrations, models
from faker import Faker

fake = Faker()


def add_client_data(apps, schema_editor):  # noqa: C901
    """Добавление информации о клиентах."""
    FakeClientData = apps.get_model("llm_request", "FakeClientData")  # noqa: N806

    FakeClientData.objects.bulk_create(
        [
            FakeClientData(
                gender=int(fake.pybool()),
                age=fake.pyfloat(min_value=18, max_value=75),
                reg_region_nm=fake.city(),
                cnt_tr_all_3m=fake.pyfloat(),
                cnt_tr_top_up_3m=fake.pyfloat(),
                cnt_tr_cash_3m=fake.pyfloat(),
                cnt_tr_buy_3m=fake.pyfloat(),
                cnt_tr_mobile_3m=fake.pyfloat(),
                cnt_tr_oil_3m=fake.pyfloat(),
                cnt_tr_on_card_3m=fake.pyfloat(),
                cnt_tr_service_3m=fake.pyfloat(),
                cnt_zp_12m=fake.pyfloat(),
                sum_zp_12m=fake.pyfloat(),
                limit_exchange_count=fake.pyfloat(),
                max_outstanding_amount_6m=fake.pyfloat(),
                avg_outstanding_amount_3m=fake.pyfloat(),
                cnt_dep_act=fake.pyfloat(),
                sum_dep_now=fake.pyfloat(),
                avg_dep_avg_balance_1month=fake.pyfloat(),
                max_dep_avg_balance_3month=fake.pyfloat(),
                app_vehicle_ind=int(fake.pybool()),
                app_position_type_nm=fake.word(),
                visit_purposes=fake.word(),
                qnt_months_from_last_visit=fake.pyfloat(),
                super_clust=fake.word(),
            )
            for i in range(100)
        ]
    )



class Migration(migrations.Migration):

    dependencies = [
        ('llm_request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeClientData',
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
                    'gender',
                    models.CharField(
                        max_length=255,
                        verbose_name='Пол клиента (0 муж, 1 жен)',
                    ),
                ),
                (
                    'age',
                    models.CharField(
                        max_length=255, verbose_name='Возраст Клиента'
                    ),
                ),
                (
                    'reg_region_nm',
                    models.CharField(max_length=255, verbose_name='Регион'),
                ),
                (
                    'cnt_tr_all_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество транзакций за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_top_up_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество приходных операций за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_cash_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций выдачи наличных за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_buy_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций оплаты покупок за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_mobile_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций оплаты связи за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_oil_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций оплаты на АЗС за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_on_card_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций переводов по карте за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_tr_service_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество операций оплаты услуг за последние 3 месяца',
                    ),
                ),
                (
                    'cnt_zp_12m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество зарплатных поступлений за 12 месяцев',
                    ),
                ),
                (
                    'sum_zp_12m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Сумма зарплатных поступлений за 12m',
                    ),
                ),
                (
                    'limit_exchange_count',
                    models.CharField(
                        max_length=255,
                        verbose_name='Общее количество изменений лимита',
                    ),
                ),
                (
                    'max_outstanding_amount_6m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Максимальная задолженность по основному долгу за 6 месяцев',
                    ),
                ),
                (
                    'avg_outstanding_amount_3m',
                    models.CharField(
                        max_length=255,
                        verbose_name='Средняя задолженность по основному долгу за 3 месяца',
                    ),
                ),
                (
                    'cnt_dep_act',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество активных срочных депозитов, имеющих текущий остаток более 1000 р',
                    ),
                ),
                (
                    'sum_dep_now',
                    models.CharField(
                        max_length=255,
                        verbose_name='Текущая общая сумма (в рублях) срочных депозитов',
                    ),
                ),
                (
                    'avg_dep_avg_balance_1month',
                    models.CharField(
                        max_length=255,
                        verbose_name='Средний баланс по всем депозитам за последний месяц',
                    ),
                ),
                (
                    'max_dep_avg_balance_3month',
                    models.CharField(
                        max_length=255,
                        verbose_name='Максимальный баланс по всем депозитам за 3 месяца',
                    ),
                ),
                (
                    'app_vehicle_ind',
                    models.CharField(
                        max_length=255, verbose_name='Наличие авто'
                    ),
                ),
                (
                    'app_position_type_nm',
                    models.CharField(
                        max_length=255,
                        verbose_name='Уровень занимаемой позиции',
                    ),
                ),
                (
                    'visit_purposes',
                    models.CharField(
                        max_length=255,
                        verbose_name='Цель последнего посещения офиса',
                    ),
                ),
                (
                    'qnt_months_from_last_visit',
                    models.CharField(
                        max_length=255,
                        verbose_name='Количество месяцев с прошлого посещения офиса',
                    ),
                ),
                (
                    'super_clust',
                    models.CharField(
                        max_length=255, verbose_name='Кластер клиента'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Данные клиентов для тестирования загрузки данных из postgres',
                'verbose_name_plural': 'Данные клиентов для тестирования загрузки данных из postgres',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.RunPython(
            add_client_data,
            migrations.RunPython.noop,
        ),
    ]
