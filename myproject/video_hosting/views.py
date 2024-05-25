from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Comment, Like
from .forms import VideoForm, CommentForm
from ..templates import *

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_hosting/video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video_hosting/video_detail.html', {'video': video})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_hosting/upload_video.html', {'form': form})

def add_comment_to_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.author = request.user  # Ассумируя, что пользователь залогинен
            comment.save()
            return redirect('video_detail', video_id=video.id)
    else:
        form = CommentForm()
    return render(request, 'video_hosting/add_comment_to_video.html', {'form': form})
