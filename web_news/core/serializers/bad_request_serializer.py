from rest_framework import serializers


class BadRequestSerializer(serializers.Serializer):
    """Status 400 Response."""

    detail = serializers.CharField(default="Bad Request")
