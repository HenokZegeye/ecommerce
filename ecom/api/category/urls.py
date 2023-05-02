from rest_framework import routers
from .views import CategoryViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)
urlpatterns = [
    path('', include(router.urls))
]