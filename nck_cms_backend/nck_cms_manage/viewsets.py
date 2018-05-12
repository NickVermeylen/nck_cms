from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.db.models import Q


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        search_query = self.request.GET.get("q")
        if search_query is not None:
            queryset = queryset.filter(Q(article_heading__icontains=search_query)
                                       | Q(article_body__icontains=search_query)).distinct()
        return queryset
