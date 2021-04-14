from django.db import models
from django.shortcuts import render, redirect
from .models import Apikey
from apikey.models import Subscription

# Create your views here.
def apiGenerate(request):
    
    if request.method == 'POST':
        try:
            new_key = Apikey(
                user = request.user,
                key_name = request.POST['keyname'],
                website = Subscription.objects.get(user='shimar'),
                key = secrets.token_urlsafe(10),
            )    
            new_key.save()
            print(f'NewKey: {request.POST["keyname"]}')
            return redirect('/apikey/')
        except Exception as e:
            print(f'NewKey, Error: {e}')
            return redirect('apikey/generate')
    website = Subscription.objects.all()
    return render(request, 'apigenerate.html', {'website': website }) #

def apiManage(request):
    apikey = Apikey.objects.all()
    return render(request, 'apimanage.html', {'apikey': apikey} )
