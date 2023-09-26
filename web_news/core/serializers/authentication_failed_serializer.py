from rest_framework import serializers


class AuthenticationFailedSerializer(serializers.Serializer):
    """Status 403 Response."""

    detail = serializers.CharField(default="Authorization header not found")
