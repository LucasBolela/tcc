from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from eagle.serializers.tracker_serializer import TrackerSerializer
from eagle.models.tracker import Tracker

# from loguru import logger
# from open_banking.tools.webhook.item_webhook import CreateItem
# from core.helpers.view_set_default_helper import ViewSetDefaultHelper
from core.serializers import (
    AuthenticationFailedSerializer,
    BadRequestSerializer,
    GatewayTimeoutSerializer,
    NotAuthorizedSerializer,
    SuccessResponseOKSerializer,
)


class TrackerViewSet(APIView):
    serializer_class = TrackerSerializer
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        summary=_("Tracker."),
        description=_("Tracker."),
        responses={
            200: TrackerSerializer,
            400: BadRequestSerializer,
            401: AuthenticationFailedSerializer,
            403: NotAuthorizedSerializer,
            504: GatewayTimeoutSerializer,
        },
    )
    def get(self, request) -> Response:
        instances = Tracker.objects.all()
        serializer = self.serializer_class(instances, many=True)
        try:
            response = serializer.data
            return Response(
                response, content_type="application/json", status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"message": "Erro amigo ;("},
                content_type="application/json",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @extend_schema(
        summary=_("Tracker."),
        description=_("Tracker."),
        responses={
            201: TrackerSerializer,
            400: BadRequestSerializer,
            401: AuthenticationFailedSerializer,
            403: NotAuthorizedSerializer,
            504: GatewayTimeoutSerializer,
        },
    )
    def post(self, request) -> Response:
        request_data = request.data
        instances = Tracker.objects.create(**request_data)
        serializer = self.serializer_class(instances)
        try:
            response = serializer.data
            return Response(
                response,
                content_type="application/json",
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response(
                {"message": "Erro amigo ;("},
                content_type="application/json",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
