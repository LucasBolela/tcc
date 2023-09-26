from rest_framework import serializers


class GatewayTimeoutSerializer(serializers.Serializer):
    """Status 504 Response."""

    detail = serializers.CharField(default="Gateway Timeout")
