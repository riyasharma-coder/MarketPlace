from django.shortcuts import render, redirect
from .models import SuccessStory
from django.contrib.auth.decorators import login_required

def story_list_view(request):
    stories = SuccessStory.objects.all().order_by('-created_at')
    return render(request, 'community/success_stories.html', {'stories': stories})

@login_required
def share_story_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        SuccessStory.objects.create(user=request.user, title=title, content=content, image=image)
        return redirect('stories')
    return render(request, 'community/share_story.html')