from django.db import models
from django.shortcuts import render, redirect
from .models import Apikey
from apikey.models import Subscription
from user.models import Domains
from django.contrib.auth import authenticate
import secrets

# Create your views here.
def apiGenerate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                new_key = Apikey(
                    user = request.user,
                    key_name = request.POST['keyname'],
                    website = Domains.objects.get(username=request.user),
                    key = secrets.token_urlsafe(10),
                )    
                new_key.save()
                print(f'NewKey: {request.POST["keyname"]}')
                return redirect('/apikey/')
            except Exception as e:
                print(f'NewKey, Error: {e}')
                return redirect('/apikey/generate')
        website = Domains.objects.filter(username=request.user)
        return render(request, 'apigenerate.html', {'website': website }) #
    else:
        return redirect('/login') 

def apiManage(request):
    if request.user.is_authenticated:
        apikey = Apikey.objects.filter(user=request.user)
        return render(request, 'apimanage.html', {'apikey': apikey} )
    else:
        return redirect('/login')
