# -*- coding: utf-8 -*-
from rest_framework import serializers
from contact.models import ContactEmail


class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = ('id', 'email', 'message')

    def create(self, validated_data):
        return ContactEmail.objects.create(**validated_data)
