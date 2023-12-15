from server.apps.g_mtg.models import Product
from server.apps.services.serializers import ModelSerializerWithPermission


class ProductSerializer(ModelSerializerWithPermission):
    """Продукт банка."""

    class Meta(object):
        model = Product
        fields = (
            'id',
            'name',
            'key_name',
            'description',
            'created_at',
            'updated_at',
            'permission_rules',
        )
