from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('register', CreateUserView, 'register')

urlpatterns = router.urls