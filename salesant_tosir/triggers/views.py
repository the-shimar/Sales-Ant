from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Triggers, UserTriggers
from builder.models import Build
from apikey.models import Subscription
from django.contrib.auth import authenticate



# Create your views here.
def newTrigger(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            try:
                user_trigger = UserTriggers( name=request.POST['TriggerName'],
                user=request.user,
                trigger_type=request.POST['TriggerType'] , 
                website=Subscription.objects.get(user='shimar'),
                build=request.POST['TriggerBuild'],
                limit=request.POST['TriggerLimit'], )
                
                user_trigger.save()
                print(f"TriggerSave Ok {request.POST['TriggerName']}")
                return redirect('/triggers/manage')
                
            except Exception as e:
                print(f"TriggerSave Error: {e}")
                return redirect('/triggers/create')

        user_trigger = UserTriggers.objects.filter(user=request.user)
        triggers_list = Triggers.objects.all()
        builder_list = Build.objects.filter(user=request.user)

        return render(request, 'triggernew.html', {'triggers_list': triggers_list,
        'builder_list': builder_list, 'user_trigger': user_trigger})
    else:
        return redirect('/login')

def manageTriggers(request):
    if request.user.is_authenticated:
        triggers_list = UserTriggers.objects.filter(user=request.user)
        return render(request, 'triggersmanage.html', { 'triggers_list': triggers_list })
    else:
        return redirect('/login')

def triggerDelete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(f'POST: All Builds of {request.POST["TriggerName"]}')
            try:
                UserTriggers.objects.get(name=request.POST['TriggerName'], user=request.user).delete()
                print(f'Deleted: {request.POST["TriggerName"]}')
            except:
                print('Not Found!')
        return redirect('/triggers/manage')
    else:
        return redirect('/login')