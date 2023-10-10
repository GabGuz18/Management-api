from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('account', UserViewSet, 'account')

urlpatterns = router.urls