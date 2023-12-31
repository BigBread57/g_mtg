from typing import Dict, Union

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin


class DefaultUserManager(UserManager):  # type: ignore
    """Менеджер для пользователей с логином email."""

    use_in_migrations = True

    def create_user(
        self,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Создание пользователя."""
        if username is None:
            username = email
        return super().create_user(
            username,
            email,
            password,
            **extra_fields,
        )

    def create_superuser(
        self,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Создание суперпользователя."""
        if username is None:
            username = email
        return super().create_superuser(
            username,
            email,
            password,
            **extra_fields,
        )


class User(  # type: ignore
    RulesModelMixin,
    AbstractUser,
    metaclass=RulesModelBase,
):
    """Кастомный класс пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        verbose_name=_('Адрес электронной почты'),
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name=_('Аватар'),
        upload_to='media',
        blank=True,
    )
    position = models.CharField(
        verbose_name=_('Должность пользователя'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    subdivision = models.CharField(
        verbose_name=_('Подразделение, в котором работает пользователь'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    middle_name = models.CharField(
        _('Отчество'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )

    objects = DefaultUserManager()  # noqa: WPS110

    class Meta(object):
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email

    @property
    def full_name(self) -> str:
        """ФИО пользователя."""
        names_elements = (self.last_name, self.first_name, self.middle_name)
        if not any(names_elements):
            return ''
        return ' '.join(filter(None, names_elements)).strip()

    @property
    def role(self) -> Union[str, Dict[int, str]]:
        """Роль пользователя."""
        if self.projects_users.all():
            return dict(
                list(self.projects_users.values_list("project", "role")),
            )
        return ""
