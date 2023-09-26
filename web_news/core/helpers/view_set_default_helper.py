from typing import Union
from core.helpers.format_response_message import format_response_message
from rest_framework.response import Response


class DefaultProperties:
    """
    You should set each property in your ViewSet to retrieve the correct data using polymorphism.
    """

    @property
    def _get_default_pagination_params(self) -> tuple:
        """
        Set the available pagination fields of the pagination_helper.
        """
        return ("limit", "page", "order_by")

    @property
    def _get_order_by_fields(self) -> tuple:
        """
        Set the available ordering fields of a Django Model.
        """
        return ()

    @property
    def _get_default_query_params(self) -> dict:
        """
        Set the available query parameters of the request.
        """
        return {}

    @property
    def _get_default_payload_fields(self) -> tuple:
        """
        Set the available payload fields of the request.
        """
        return ()

    @property
    def _get_required_payload_fields(self) -> tuple:
        """
        Set the required payload fields of the request.
        """
        return ()


class ViewSetDefaultHelper(DefaultProperties):
    view_set_method: str = ...
    serializer_class: object = ...

    def http_response(
        self, message: Union[str, dict], status_code: int = 200
    ) -> Response:
        """
        Generates an HTTP response with the given message and status code.
        """
        response = (
            message
            if (isinstance(message, dict) or isinstance(message, list))
            else {"message": message}
        )
        return Response(
            response,
            content_type="application/json",
            status=status_code,
        )

    def http_response_error(
        self, message: Union[str, dict, Exception], status_code: int = 400
    ) -> Response:
        """
        Generates an HTTP response with the given message and status code formatting with the format_response_message helper.
        This should only be used when you need to format an exception message (e.g., Exception, HTTP404, etc.).
        Otherwise, use the http_response method.
        """
        return format_response_message(
            _error=message, status_code=status_code, method=self.view_set_method
        )
