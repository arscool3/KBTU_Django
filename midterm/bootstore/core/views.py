from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.utils.decorators import method_decorator
from core.models import Book, Author, Order, OrderItem, UserProfile, Publisher
from core.forms import BookForm, AuthorForm, UpdateUserForm, OrderForm
from django.views import View
from django.contrib.auth.decorators import login_required

def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


@decorators.permission_required('core.can_add_Books', login_url='login')
def add_books(request):
    return basic_form(request, BookForm)


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


@decorators.login_required(login_url='login')
def get_books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_books')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})


def update_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('get_books')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'update_author.html', {'form': form})

@method_decorator(login_required(login_url='/login'), name='dispatch')
class OrderView(View):
    def get(self, request):
        user_orders = Order.objects.filter(user=request.user)
        order_items = OrderItem.objects.filter(order__user=request.user)

        context = {
            'user_orders': user_orders,
            'order_items': order_items,
        }

        return render(request, 'order.html', context)

@login_required
def update_user_info(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'update_user_info.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for book_id in request.POST.getlist('books'):
                book = Book.objects.get(id=book_id)
                order.books.add(book)
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})


def list_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers': publishers})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile.html', {'profile': profile})

