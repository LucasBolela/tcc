from rest_framework import serializers

from eagle.models.web_sites import SiteDeNoticias


class WebSiteSerializer(serializers.ModelSerializer):
    """
    Serializer for WebSite model to return the item data
    """

    class Meta:
        model = SiteDeNoticias
        fields = "__all__"
