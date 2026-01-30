from django.shortcuts import render
from .models import Center

def center_map_view(request):
    centers = Center.objects.all()
    return render(request, 'centers/map_view.html', {'centers': centers})