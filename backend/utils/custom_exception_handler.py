from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc=exc, context=context)

    exception_class = exc.__class__.__name__
    print(exception_class)
    if exception_class == "AuthenticationFailed":
        response.data = {"error": "Invalid email or Password. Please try again."}
    if exception_class == "NotAuthenticated":
        response.data = {"error": "Please login first."}
    if exception_class == "InvalidToken":
        response.data = {
            "error": "Your authentication token has expired, please login again."
        }

    return response
