from rest_framework import status, views
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# 投稿作成

class CreatePostView(views.APIView):
    permission_classes = []  # パーミッションクラスを空のリストに設定

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 投稿一覧表示
class ListPostsView(views.APIView):
    def get_queryset(self):
        return Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


class PostAPIView(APIView):
    def get_queryset(self):
        return Post.objects.all()

    def get(self, request, **kwargs):
        try:
            prace_id = kwargs['prace_id']
            post = self.get_queryset().filter(PraceID_id=prace_id)
            serializer = PostSerializer(post,many=True)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=404)

