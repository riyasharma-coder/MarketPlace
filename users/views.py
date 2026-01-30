from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User 
from exchange.models import Item, SwapRequest
from community.models import SuccessStory

def register_view(request):
    if request.method == 'POST':
        # Frontend se data lena
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        role = request.POST.get('role')
        
        # Naya user create karna (Hashing included)
        user = User.objects.create_user(
            username=u_name, 
            email=email, 
            password=pwd, 
            role=role
        )
        login(request, user)
        # Registration ke baad seedha profile par bhejenge
        return redirect('profile') 
    
    return render(request, 'users/register.html')

@login_required
def profile_view(request):
    # User ke apne items
    user_items = Item.objects.filter(owner=request.user).order_by('-created_at')
    
    # User ki stories
    user_stories = SuccessStory.objects.filter(user=request.user).order_by('-created_at')
    
    # Kitne swaps successful huye (Items owned by user that are marked as swapped)
    swaps_completed = Item.objects.filter(owner=request.user, is_swapped=True).count()

    return render(request, 'users/profile.html', {
        'items': user_items,
        'stories': user_stories,
        'swaps_count': swaps_completed
    })
