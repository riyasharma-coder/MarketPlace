from django.shortcuts import render
from .models import Center
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def center_map_view(request):
    try:
        centers = Center.objects.all()
        if not centers.exists():
            context = {
                'centers': [],
                'message': 'No recycling centers available at the moment.'
            }
        else:
            context = {'centers': centers}
        return render(request, 'centers/map_view.html', context)
    except Exception as e:
        return render(request, 'centers/map_view.html', {
            'error': 'Error loading centers. Please try again later.',
            'centers': []
        })