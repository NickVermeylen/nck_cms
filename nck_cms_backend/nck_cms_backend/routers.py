from rest_framework import routers
from nck_cms_manage.viewsets import ArticleViewSet
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
