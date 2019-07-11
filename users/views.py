# -*- coding: utf-8 -*-
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(
                user, context=self.get_serializer_context()).data,
        })
