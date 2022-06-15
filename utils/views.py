from django.http import JsonResponse

def error_404(request, exception):
    message=(f'404 Not Found: {request.path}')
    data = {
        'message': message,
        'status_code': 404
    }
    return JsonResponse(data, status=404)

def error_500(request):
    message=(f'500 Internal Server Error: {request.path}')
    data = {
        'message': message,
        'status_code': 500
    }
    return JsonResponse(data, status=500)