from typing import Union
from rest_framework.response import Response
from core.helpers.format_response_message import format_response_message
from core.exceptions.generic_validations_error import GenericValidationError


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
    def _get_required_fields(self) -> tuple:
        """
        Set the available ordering fields of a Django Model.
        """
        return ("link", "file")


class ViewSetReaderHelper(DefaultProperties):
    view_set_method: str = ...
    serializer_class: object = ...

    def validate_query_params(self, request_params: dict) -> dict:
        """
        Validates a dictionary of request parameters to ensure they are valid.
        ----
        The function iterates over the keys in the request_params dictionary and checks if each parameter
        is a valid parameter. If a parameter is not valid, a GenericValidationError is raised with a message
        indicating which parameter is invalid. Otherwise, the function returns the validated request_params.
        """
        for param in request_params:
            if (
                param not in self._get_default_query_params.keys()
                and param not in self._get_default_pagination_params
            ):
                raise GenericValidationError(
                    message=f"Parâmetro {param.upper()} Inválido.",
                    status_code=422,
                )
        return request_params

    def validate_payload(self, request_data: dict, blank: bool = True) -> dict:
        """
        Validate the payload data to ensure it contains only valid fields.
        """
        if blank or request_data:
            for param in request_data.keys():
                if param not in self._get_default_payload_fields:
                    raise GenericValidationError(
                        message=f"Campo '{param}' Inválido.",
                        status_code=422,
                    )
            return request_data
        raise GenericValidationError(message="Payload Inválido.", status_code=422)

    def validate_required_payload_fields(self, request_data: dict) -> dict:
        """
        Validate the payload data to ensure all the required fields were sent
        """
        for required_param in self._get_required_payload_fields:
            if required_param not in request_data.keys():
                raise GenericValidationError(
                    message=f"Campo '{required_param}' não enviado.",
                    status_code=422,
                )

        return request_data

    def validate_required_fields_get(self, request_data: dict) -> dict:
        """
        Validate the payload data to ensure all the required fields were sent
        """

        for required_param in self._get_required_fields:
            if required_param in request_data.keys():
                return request_data, required_param

        raise GenericValidationError(
            message=f"Campos 'link' e file' não enviados.",
            status_code=422,
        )

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
