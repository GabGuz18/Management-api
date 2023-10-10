from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('products', ProductsViewSet, 'products')

urlpatterns = router.urls