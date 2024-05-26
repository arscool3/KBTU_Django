from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, decorators
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tag, Question, Answer, Vote, Comment
from .serializers import TagSerializer, QuestionSerializer, AnswerSerializer, VoteSerializer, CommentSerializer
from .forms import QuestionForm, AnswerForm, TagForm, SignUpForm, LoginForm
from django.shortcuts import render, get_object_or_404, redirect
from .tasks import add


# Welcome, Page
def welcome(request):
    return render(request, 'welcome.html')


# Note that's user should login
def should_login(request):
    return render(request, 'should_login.html')


# Home Page
@decorators.login_required(login_url='should_login')
def home(request):
    return render(request, 'home.html')


# Logout, then Welcome Page
@decorators.login_required(login_url='welcome')
def user_logout(request):
    logout(request)
    return redirect('welcome')


# Sign Up Page
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Sign In
def signin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        question = get_object_or_404(Question, pk=pk)
        if question.author == request.user:
            # return Response({'status': 'You cannot vote for your own question'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        if Vote.objects.filter(user=request.user, question=question).exists():
            # return Response({'status': 'You have already voted for this question'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        Vote.objects.create(user=request.user, question=question, is_upvote=True)
        question.upvotes += 1
        question.save()
        return render(request, 'question_detail.html', {'question': question})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        question = get_object_or_404(Question, pk=pk)
        if question.author == request.user:
            # return Response({'status': 'You cannot vote for your own question'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        if Vote.objects.filter(user=request.user, question=question).exists():
            # return Response({'status': 'You have already voted for this question'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        Vote.objects.create(user=request.user, question=question, is_upvote=False)
        question.downvotes += 1
        question.save()
        # return Response({'status': 'Question downvoted'})
        return render(request, 'question_detail.html', {'question': question})


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        answer = get_object_or_404(Answer, pk=pk)
        question = get_object_or_404(Question, pk=pk)
        if answer.author == request.user:
            # return Response({'status': 'You cannot vote for your own answer'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        if Vote.objects.filter(user=request.user, answer=answer).exists():
            # return Response({'status': 'You have already voted for this answer'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        Vote.objects.create(user=request.user, answer=answer, is_upvote=True)
        answer.upvotes += 1
        answer.save()
        return render(request, 'question_detail.html', {'question': question})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        answer = get_object_or_404(Answer, pk=pk)
        question = get_object_or_404(Question, pk=pk)
        if answer.author == request.user:
            # return Response({'status': 'You cannot vote for your own answer'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        if Vote.objects.filter(user=request.user, answer=answer).exists():
            # return Response({'status': 'You have already voted for this answer'}, status=400)
            return render(request, 'question_detail.html', {'question': question})
        Vote.objects.create(user=request.user, answer=answer, is_upvote=False)
        answer.downvotes += 1
        answer.save()
        # return Response({'status': 'Answer downvoted'})
        return render(request, 'question_detail.html', {'question': question})


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def questions_list(request):
    questions = Question.objects.all()
    return render(request, 'questions_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'question_detail.html', {'question': question})


@decorators.login_required(login_url='should_login')
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            form.save_m2m()
            return redirect('questions_list')
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})


@decorators.login_required(login_url='should_login')
def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if question.author == request.user:
        messages.error(request, "You cannot answer your own question.")
        return redirect('question_detail', question_id=question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'create_answer.html', {'form': form, 'question': question})


def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags_list')
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})


def add_view(request):
    result = add.delay(4, 6)
    return HttpResponse(f'Task ID: {result.id}')
