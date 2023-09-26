from rest_framework import serializers


class NotAuthorizedSerializer(serializers.Serializer):
    """Status 401 Response."""

    detail = serializers.CharField(default="Not authorized")
