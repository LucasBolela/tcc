class GenericValidationError(Exception):
    """
    This class represents an Exception that is raised when there is an error
    validating something.
    Initializes the Exception base class.

    Attributes:
    message (str/dict): The error message.
    status_code (int): The HTTP status code.
    """

    def __init__(self, message="Error!", status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
