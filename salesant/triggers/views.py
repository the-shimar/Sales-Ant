from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Triggers, UserTriggers
from builder.models import Build
from apikey.models import Subscription


# Create your views here.
def newTrigger(request):

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

    user_trigger = UserTriggers.objects.all()
    triggers_list = Triggers.objects.all()
    builder_list = Build.objects.all()

    return render(request, 'triggernew.html', {'triggers_list': triggers_list,
     'builder_list': builder_list, 'user_trigger': user_trigger})

def manageTriggers(request):
    triggers_list = UserTriggers.objects.all()
    return render(request, 'triggersmanage.html', { 'triggers_list': triggers_list })

def triggerDelete(request):
    if request.method == 'POST':
        print(f'POST: All Builds of {request.POST["TriggerName"]}')
        try:
            UserTriggers.objects.get(name=request.POST['TriggerName']).delete()
            print(f'Deleted: {request.POST["TriggerName"]}')
        except:
            print('Not Found!')
    return redirect('/triggers/manage')