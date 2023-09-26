import json
from datetime import datetime
from json import JSONDecodeError
from typing import Union

from loguru import logger


def format_error_message(
    message: str, method: str, exception_log: Exception = "None"
) -> Union[str, dict]:
    """
    Format the error message for HTTP requests or other exceptions.

    :param message: The error message to be formatted.
    :param method: The method where the error was raised.
    :param exception_log: Additional information about the exception (e.g. the traceback). Default is "None".
    :return: A dictionary containing the formatted error message, the method where the error was raised, the current datetime, and the additional exception information.
    """
    log_response = {
        "method": method,
        "datetime": datetime.now().isoformat(),
    }

    response: dict = {}
    try:
        response["exception_log"] = json.loads(exception_log.response.text)
    except (JSONDecodeError, Exception):
        response["exception_log"] = str(exception_log)

    response["message"] = str(message)
    log_response.update(response)
    logger.error(response)
    return response
