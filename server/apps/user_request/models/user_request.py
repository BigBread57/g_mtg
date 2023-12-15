
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.enums import ClientType, RequestStatus, SuccessType


class UserRequest(AbstractBaseModel):
    """Запрос пользователя."""

    project_sale_channel = models.ForeignKey(
        to='g_mtg.ProjectSaleChannel',
        on_delete=models.CASCADE,
        verbose_name=_('Канал связи проетка'),
        related_name='users_requests',
        db_index=True,
    )
    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='users_requests',
        db_index=True,
    )
    client_id = models.CharField(
        verbose_name=_('ID клиента из сторонних ресурсов'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    source_client_info = models.CharField(
        verbose_name=_('Источник информации о клиенте'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    client_data = models.JSONField(
        verbose_name=_('Данные о клиенте'),
    )
    client_data_decoding = models.JSONField(
        verbose_name=_('Расшифровка данных о клиенте'),
    )
    status = models.CharField(
        verbose_name=_('Статус запроса'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=RequestStatus.choices,
        default=RequestStatus.IN_PROGRESS,
    )
    success_type = models.CharField(
        verbose_name=_('Тип успеха'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=SuccessType.choices,
        default=SuccessType.UNDEFINED,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Запрос пользователя')
        verbose_name_plural = _('Запросы пользователей')

    def __str__(self):
        return f'{self.project_sale_channel} - {self.user}'
