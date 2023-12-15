from django.utils.translation import gettext_lazy as _
from drf_nova_router.api_router import ApiRouter
from rest_framework.routers import APIRootView

from server.apps.g_mtg.api.views import (
    ProductViewSet,
    # ProjectSaleChannelViewSet,
    # ProjectUserViewSet,
    ProjectViewSet,
    SaleChannelViewSet,
)


class GMtgAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = _('Приложение G-MTG')
    name = _('g_mtg')


router = ApiRouter()

router.APIRootView = GMtgAPIRootView
router.register('sales-channels', SaleChannelViewSet, 'sales-channels')
# router.register('projects-users', ProjectUserViewSet, 'projects-users')
# router.register(
#     'projects-sales-channels',
#     ProjectSaleChannelViewSet,
#     'projects-sales-channels',
# )
router.register('projects', ProjectViewSet, 'projects')
router.register('products', ProductViewSet, 'products')
