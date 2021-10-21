# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from contact.serializers import ContactEmailSerializer
from contact.models import ContactEmail


class ListContactView(generics.ListCreateAPIView):
    serializer_class = ContactEmailSerializer
    queryset = ContactEmail.objects.all()
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = self.get_queryset().none()
        if request.user.is_superuser or request.user.is_staff:
            queryset = self.get_queryset()
        serializer = ContactEmailSerializer(queryset, many=True)
        return Response(serializer.data)