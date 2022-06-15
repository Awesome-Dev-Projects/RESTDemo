from rest_framework.views import exception_handler


def custome_exception_handler(exc, context):
    """
    Custom exception handler.
    """
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'NotFound': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'AuthenticationFailed': _handle_failed_authentication_error,
        'InvalidToken': _handle_token_error,
        'TokenError': _handle_token_error,
        'MethodNotAllowed': _handle_generic_error,
    }
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_generic_error(exc, context, response):
    """
    Handle generic errors.
    """
    return response


def _handle_authentication_error(exc, context, response):
    """
    Handle authentication errors.
    """
    response.data = {
        'error': 'Please login to access this resource',
        'status_code': response.status_code
    }
    return response

def _handle_failed_authentication_error(exc, context, response):
    """
    Handle authentication errors.
    """
    response.data = {
        'error': 'Invalid credentials provided',
        'status_code': response.status_code
    }
    return response

def _handle_token_error(exc, context, response):
    """
    Handle token errors.
    """
    response.data = {
        'error': 'Invalid token provided or token expired',
        'status_code': response.status_code
    }
    return response
