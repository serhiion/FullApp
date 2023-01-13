from rest_framework import routers
from item.api.api import ItemViewSet

router = routers.DefaultRouter()
router.register('api/item', ItemViewSet, 'item')

urlpatterns = router.urls
