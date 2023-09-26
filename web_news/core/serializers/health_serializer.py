import arrow
from rest_framework import serializers


class HealthCheckResponseSerializer(serializers.Serializer):
    """Response Ok."""

    status = serializers.CharField(default="OK")
    database = serializers.CharField(default="OK (1)")
    worker = serializers.CharField(default="OK (Done)")
    time = serializers.CharField(default=arrow.utcnow().isoformat())
