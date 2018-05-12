from rest_framework import routers
from nck_cms_manage.viewsets import ArticleViewSet
from nck_cms_manage.viewsets import CustomerViewSet
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
router.register('customer', CustomerViewSet)
