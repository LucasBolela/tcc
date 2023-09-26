from rest_framework import serializers


class SuccessResponseOKSerializer(serializers.Serializer):
    """Status 200 Response."""

    detail = serializers.CharField(default="Success!")
