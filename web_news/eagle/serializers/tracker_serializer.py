from rest_framework import serializers

from eagle.models.tracker import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    """
    Serializer for Tracker model to return the item data
    """

    class Meta:
        model = Tracker
        fields = "__all__"
