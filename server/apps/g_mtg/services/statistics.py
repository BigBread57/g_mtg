from typing import Any, Dict, List

from django.db.models import F, Count

from server.apps.g_mtg.models import ProjectUser, ProjectSaleChannel, Project
from server.apps.llm_request.models import RequestData
from server.apps.services.enums import SuccessType


def get_statistics(
    projects_id: List[str],
) -> Dict[str, Any]:
    """Формирование статистики по проекту."""
    if not projects_id:
        projects_id = Project.objects.values_lust('id', flat=True)

    if len(projects_id) > 1:

        return {
            'die': {
                'name': 'Числовые показатели',
                'data': [
                    {
                        'type': 'die',
                        'name': 'Общее количество пользователей в проектах',
                        'value': ProjectUser.objects.all().count(),
                    },
                    {
                        'type': 'die',
                        'name': 'Общее количество каналов в проектах',
                        'value': ProjectSaleChannel.objects.all().count(),
                    },
                    {
                        'type': 'die',
                        'name': 'Общее количество запросов',
                        'value': RequestData.objects.all().count(),
                    },
                ],
            },
            'products': {
                'name': 'Статистика по продуктам',
                'data': [
                    {
                        'type': 'circular',
                        'name': 'Статистика по продуктам в проектах',
                        'value': RequestData.objects.filter(
                            project_sale_channel__project__in=projects_id,
                        ).values(
                            product=F('project_sale_channel__project__product'),
                        ).annotate(count=Count('id')).order_by('-count'),
                    },
                    {
                        'type': 'circular',
                        'name': 'Статистика по типу успешности в рамка продукта',
                        'value': RequestData.objects.filter(
                            project_sale_channel__project__in=projects_id,
                            success_type__in={SuccessType.SOLD, SuccessType.INTEREST},
                        ).values(
                            'project_sale_channel__project__product'
                        ).annotate(count=Count('id')).order_by('-count'),
                    },
                ],
            },
            'sale_channel': {
                'name': 'Статистика по каналам продаж',
                'data': [
                    {
                        'type': 'columnar',
                        'name': 'Популярность каналов продаж',
                        'value': ProjectSaleChannel.objects.filter(
                            project__in=projects_id,
                        ).values(
                            'sale_channel'
                        ).annotate(count=Count('id')).order_by('-count'),
                    },
                    {
                        'type': 'columnar',
                        'name': 'Количество запросов для каналов продаж',
                        'value': RequestData.objects.filter(
                            project_sale_channel__project__in=projects_id,
                        ).values(
                            'project_sale_channel__sale_channel',
                        ).annotate(count=Count('id')).order_by('-count'),
                    },
                ],
            },
            'request_data': {
                'name': 'Статистика по запросам',
                'data': [
                    {
                        'type': 'circular',
                        'name': 'Статистика по успешности запросов в проектах',
                        'value': RequestData.objects.filter(
                            project_sale_channel__project__in=projects_id,
                        ).values(
                            'success_type',
                        ).annotate(count=Count('id')).order_by('-count'),
                    },
                ],
            },
        }

    return {
        'die': {
            'name': 'Числовые показатели',
            'data': [
                {
                    'type': 'die',
                    'name': 'Общее количество пользователей в проектах',
                    'value': ProjectUser.objects.all().count(),
                },
                {
                    'type': 'die',
                    'name': 'Общее количество каналов в проектах',
                    'value': ProjectSaleChannel.objects.all().count(),
                },
                {
                    'type': 'die',
                    'name': 'Общее количество запросов',
                    'value': RequestData.objects.all().count(),
                },
            ],
        },
        'products': {
            'name': 'Статистика по продуктам',
            'data': [
                {
                    'type': 'circular',
                    'name': 'Статистика по продуктам в проектах',
                    'value': RequestData.objects.filter(
                        project_sale_channel__project__in=projects_id,
                    ).values(
                        product=F('project_sale_channel__project__product'),
                    ).annotate(count=Count('id')).order_by('-count'),
                },
                {
                    'type': 'circular',
                    'name': 'Статистика по типу успешности в рамка продукта',
                    'value': RequestData.objects.filter(
                        project_sale_channel__project__in=projects_id,
                        success_type__in={SuccessType.SOLD, SuccessType.INTEREST},
                    ).values(
                        'project_sale_channel__project__product'
                    ).annotate(count=Count('id')).order_by('-count'),
                },
            ],
        },
        'sale_channel': {
            'name': 'Статистика по каналам продаж',
            'data': [
                {
                    'type': 'columnar',
                    'name': 'Популярность каналов продаж',
                    'value': ProjectSaleChannel.objects.filter(
                        project__in=projects_id,
                    ).values(
                        'sale_channel'
                    ).annotate(count=Count('id')).order_by('-count'),
                },
                {
                    'type': 'columnar',
                    'name': 'Количество запросов для каналов продаж',
                    'value': RequestData.objects.filter(
                        project_sale_channel__project__in=projects_id,
                    ).values(
                        'project_sale_channel__sale_channel',
                    ).annotate(count=Count('id')).order_by('-count'),
                },
            ],
        },
        'request_data': {
            'name': 'Статистика по запросам',
            'data': [
                {
                    'type': 'circular',
                    'name': 'Статистика по успешности запросов в проектах',
                    'value': RequestData.objects.filter(
                        project_sale_channel__project__in=projects_id,
                    ).values(
                        'success_type',
                    ).annotate(count=Count('id')).order_by('-count'),
                },
            ],
        },
    }

