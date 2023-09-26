import json
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema

from rest_framework.response import Response
from rest_framework.views import APIView
from core.exceptions.generic_validations_error import GenericValidationError
from core.helpers.set_encoder import set_encoder

from eagle.helpers.validators.reader.view_set_reader_validate import ViewSetReaderHelper
from eagle.helpers import read_document_content
from eagle.models import Tracker
from core.serializers import (
    AuthenticationFailedSerializer,
    BadRequestSerializer,
    GatewayTimeoutSerializer,
    NotAuthorizedSerializer,
    SuccessResponseOKSerializer,
)


class ReaderViewSet(APIView, ViewSetReaderHelper):
    serializer_class = SuccessResponseOKSerializer
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        summary=_("Read PDF."),
        description=_(
            "A PDF reader that receive a link or file and return its content."
        ),
        responses={
            200: SuccessResponseOKSerializer,
            400: BadRequestSerializer,
            401: AuthenticationFailedSerializer,
            403: NotAuthorizedSerializer,
            504: GatewayTimeoutSerializer,
        },
    )
    def post(self, request) -> Response:
        try:
            request_data, isFile = self.validate_required_fields_get(request.data)
            content = read_document_content(
                isFile=isFile == "file",
                path=request_data.get("link"),
                file=request_data.get("file"),
            )
            response = {"message": "Success", "data": content}
            # trace = {
            #     "task": "ReaderViewSet.get",
            #     "success": True,
            #     "response": json.dumps(response, default=set_encoder),
            # }

            # Tracker.objects.create(**trace)

            return self.http_response(message=response, status_code=200)
        except GenericValidationError as _error:
            return self.http_response(
                message=_error.message, status_code=_error.status_code
            )
        except Exception as _error:
            return self.http_response(message=_error.args[0], status_code=500)
