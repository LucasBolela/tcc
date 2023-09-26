from typing import Union

from rest_framework.response import Response
from loguru import logger

from core.helpers.format_error_message import format_error_message


def format_response_message(
    _error: Union[dict, Exception], status_code: int, method: str = ""
) -> Response:
    """
    Formats a response message for an error, including the error message and status code.

    :param _error: The error message or exception that occurred. (Union[dict, Exception])
    :param status_code: The HTTP status code for the error. (int)
    :param method: The method where the error occurred. (str)
    :return: A response object with the formatted error message and status code. (Response)
    """
    error_message = format_error_message(
        message=_error,
        method=method,
        exception_log=_error,
    )
    logger.error(error_message)
    return Response(
        {"message": error_message["message"]},
        content_type="application/json",
        status=status_code,
    )
