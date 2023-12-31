from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from articles.serializers import ArticleSerializer
from articles.models import Article
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser


class ArticleCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (JSONParser,)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if obj.author != request.user:
            raise PermissionDenied("게시글 작성자만 수정할 수 있습니다.")


class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if obj.author != request.user:
            raise PermissionDenied("게시글 작성자만 삭제할 수 있습니다.")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "게시글이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT
        )
