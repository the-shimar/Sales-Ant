from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Domains

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        domains = Domains.objects.filter(username=request.user.username)
        return render(request, 'index.html', {'Domains': domains})
    else:
        return redirect('/login')
    
def purchase_domain(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                purchase = Domains(
                    website = request.POST['website'],
                    username = request.user.username,
                    plan = request.POST['plan_input']
                )
                purchase.save()
                print(f'OK {request.user.username}')
            except Exception as e:
                print(f'Error Domain: {e}')
        return redirect('/')
    else:
        return ('/login')

def profile_view(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/login')

def login_view(request):
    print(f'OK {request.user.is_authenticated}')
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                print(f'Hellooo {request.POST["username"]}')
                return redirect('/')
            # A backend authenticated the credentials
            else:
                print('Not found!')
                redirect('/login')
        return render(request, 'login.html')
    else:
        return redirect('/')
    

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                user.first_name = request.POST['first_name']
                if request.POST['last_name']:
                    user.last_name = request.POST['last_name']
                user.save()
                user_obj = User.objects.all()
                print(f'OK, {user_obj}')
                return redirect('/login')
                
            except Exception as e:
                print(f'Signup Error: {e}')
                return redirect('/signup')
        return render(request, 'signup.html')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login')