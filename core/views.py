from django.http import JsonResponse
from django.db import connection

def health_check(request):
    data = {"status": "online"}
    try:
        connection.ensure_connection()
        data["database"] = "connected"
    except Exception:
        data["database"] = "disconnected"
        return JsonResponse(data, status=500)

    return JsonResponse(data, status=200)