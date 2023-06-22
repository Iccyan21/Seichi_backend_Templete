from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from django.conf import settings
from django.contrib.auth import login, logout

from .models import AccessToken, User

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework import permissions


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(GenericAPIView):
    """ログインAPIクラス"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(UserID=serializer.validated_data["UserID"])
            userid = serializer.validated_data['UserID']
            token = AccessToken.create(user)
            return Response({'detail': "ログインが成功しました。", 'error': 0, 'token': token.token, 'UserID': userid})
        return Response({'error': 1}, status=HTTP_400_BAD_REQUEST)


# 新規登録処理
# これは新規登録用のシリアルライザー、新規登録に必要なフィールドだけを記述
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    print("RegisterView")
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # すでにEmailが使われている場合
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                print("email")
                return Response({'error': 1}, status=HTTP_400_BAD_REQUEST)

            # パスワードと確認パスワードが一致しない場合
            if serializer.validated_data['password'] != request.data['password_confirmation']:
                print("password")
                return Response({'error': 2}, status=HTTP_400_BAD_REQUEST)


            # UserIDがすでに使われていた場合
            if User.objects.filter(UserID=serializer.validated_data['UserID']).exists():
                print("UserID")
                return Response({'error': 3}, status=HTTP_400_BAD_REQUEST)

            # エラーなし
            try:
                serializer.save()
            except:
                # データベースエラー
                print("データベースエラー")
                return Response({'error': 11}, status=HTTP_500_INTERNAL_SERVER_ERROR)
            
            

            return Response(serializer.data, status=HTTP_201_CREATED)
        print("バリデーションエラー")
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

