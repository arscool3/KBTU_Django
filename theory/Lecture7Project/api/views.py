from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import *
from django.http import JsonResponse
# Create your views here.

def getUsers(request):
    if request.method == 'GET':
        users = Userr.objects.get_users()
        return render(request, 'users.html', {'users': users})

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            existing_user = Userr.objects.does_user_exist(email=email)
            if existing_user:
                return redirect(request, 'main.html', {'full_name': full_name + " again!"})
            Userr.objects.create(full_name=full_name, email=email)

            return render(request, 'main.html', {'full_name': full_name})
    else:
        form = PostForm()

    return render(request, 'create_user.html', {'form': form})

def get_all_commentaries(request):
    commentaries = Commentary.objects.get_commentaries_desc()
    data = [{'id': comment.id, 'user': comment.user.full_name, 'text': comment.text, 'commentary_type': comment.commentary_type_id.name, 'official_answer': comment.official_answer.text, 'public':comment.public} for comment in commentaries]
    form = CommentaryForm()
    return render(request, 'main.html', {'commentaries': data, 'form': form})

def get_commentary_by_id(request, commentary_id):
    commentary = Commentary.objects.get(id=commentary_id)
    data = {'id': commentary.id, 'user': commentary.user.full_name, 'text': commentary.text}
    return JsonResponse(data, safe=False)

def get_comments_by_user(request, user_id):
    try:
        commentaries = Commentary.objects.filter(user_id=user_id)
        data = [{'user': Userr.objects.get(id=user_id).full_name,'id': comment.id, 'text': comment.text, 'commentary_type': comment.commentary_type_id.name} for comment in commentaries]
        return JsonResponse({'commentaries': data})
    except Commentary.DoesNotExist:
        return JsonResponse({'error': 'User does not have any commentaries'})

@csrf_exempt
def create_commentary(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        official_answer_id = request.POST.get('official_answer_id')
        commentary_text = request.POST.get('commentary_text')
        commentary_type_id = request.POST.get('commentary_type_id')
        public = request.POST.get('public', False)

        user = get_object_or_404(Userr, pk=user_id)
        official_answer = get_object_or_404(OfficialAnswer, pk=official_answer_id)
        commentary_type = get_object_or_404(CommentaryType, pk=commentary_type_id)

        new_commentary = Commentary.objects.create(
            user=user,
            text=commentary_text,
            official_answer=official_answer,
            commentary_type_id=commentary_type,
            public=public
        )
        return JsonResponse({'success': 'Commentary created successfully', 'commentary_id': new_commentary.id})

@csrf_exempt
def delete_commentary(request, commentary_id):
    try:
        commentary = Commentary.objects.get(id=commentary_id)
        if request.method == 'POST':
            commentary.delete()
            return JsonResponse({'success': f'Commentary with ID {commentary_id} deleted successfully'})
    except Commentary.DoesNotExist:
        return JsonResponse({'error': 'Commentary not found'})

@csrf_exempt
def create_official_answer(request):
    if request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            text = request.POST['text']
            user = Userr.objects.get(id=user_id)
            new_official_answer = OfficialAnswer.objects.create(
                user=user,
                text=text
            )

            return JsonResponse({'success': f'Official Answer with ID {new_official_answer.id} created successfully'})
        except Userr.DoesNotExist:
            return JsonResponse({'error': 'User not found'})