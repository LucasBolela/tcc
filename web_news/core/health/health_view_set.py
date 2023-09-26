import arrow
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    throttle_classes,
)
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from core.serializers import HealthCheckResponseSerializer


@require_http_methods(["GET", "OPTIONS"])
@extend_schema(
    summary=_("Health Check endpoint"),
    description=_("Return simple health check."),
    responses={200: HealthCheckResponseSerializer},
    tags=["health"],
)
@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def health_check_view_set(request: Request) -> Response:
    """Return health check.

    All text here is available when accessing /api/health in DRF Browser.

    :param request: Django Rest Framework Request object
    :return: Response
    """

    payload = {
        "service": f"core ({settings.ENV})",
        "status": "Running" if settings.SECRET_KEY else "There may be issues ;(",
        "time": arrow.utcnow().isoformat(),
    }
    return Response(payload)
