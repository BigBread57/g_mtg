from rest_framework import serializers

from server.apps.g_mtg.api.serializers import BaseProductSerializer
from server.apps.g_mtg.api.serializers.nested import (
    BaseProjectSaleChannelSerializer,
)
from server.apps.g_mtg.models import Project
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class ListProjectSerializer(ModelSerializerWithPermission):
    """Список проектов."""

    product = BaseProductSerializer()

    class Meta(object):
        model = Project
        fields = (
            'id',
            'product',
            'name',
            'description',
            'created_at',
            'updated_at',
            'permission_rules',
        )


class ProjectSerializer(ModelSerializerWithPermission):
    """Проект."""

    product = BaseProductSerializer()
    users = BaseUserSerializer(many=True)
    projects_sales_channels = BaseProjectSaleChannelSerializer(many=True)

    class Meta(object):
        model = Project
        fields = (
            'id',
            'product',
            'name',
            'description',
            'users',
            'projects_sales_channels',
            'created_at',
            'updated_at',
            'permission_rules',
        )


class CreateProjectSerializer(serializers.ModelSerializer):
    """Создание проекта."""

    class Meta(object):
        model = Project
        fields = (
            'id',
            'product',
            'name',
            'description',
        )


class UpdateProjectSerializer(serializers.ModelSerializer):
    """Изменение проект."""

    class Meta(object):
        model = Project
        fields = (
            'id',
            'name',
            'description',
        )
