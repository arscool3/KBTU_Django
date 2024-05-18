from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from final.settings import LOGIN_REDIRECT_URL, LOGIN_URL

from .serializers import CustomerSerializer,ManufacturerSerializer,CategorySerializer,ProductSerializer,HistoryItemSerializer,CommentSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-username')
    serializer_class = CustomerSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('-username')
    serializer_class = ManufacturerSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-name')
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    @action(detail=True, methods=['get'])
    def get_products_by_cat(self, request, pk=None):
        cat = self.get_object()
        prods = Product.objects.filter(category=cat.id)
        serializer = self.get_serializer(prods, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
class HistoryItemViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all().order_by('-date')
    serializer_class = HistoryItemSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    @action(detail=True, methods=['get'])
    def get_history_by_user(self, request, pk=None):
        user = self.get_object().user
        hist = HistoryItem.objects.filter(user=user)
        serializer = self.get_serializer(hist, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-text')
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect(LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()
        return render(request, 'form.html', {'form':form,'entity':'Log in'})

@login_required(login_url=LOGIN_URL)     
def signout(request):
    logout(request)
    return redirect('/')
            
def signup(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            newcust = Customer(user=newuser, balance=0.0)
            newcust.save()
            return redirect('/')
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = CustomerForm()
        return render(request, 'form.html', {'form':form,'entity':'Sign up'})

def signup_mfr(request):
    if request.method=="POST":
        username = request.POST['username']
        descr = request.POST['descr']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            newcust = Customer(user=newuser, balance=0.0)
            newcust.save()
            return redirect('/')
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = CustomerForm()
        return render(request, 'form.html', {'form':form,'entity':'Sign up'})