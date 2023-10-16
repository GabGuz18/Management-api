from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, 'categories')
router.register('products', ProductsViewSet, 'products')
router.register('ingredients', IngredientsViewSet, 'ingredients')

urlpatterns = router.urls