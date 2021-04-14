from os import name
from django.shortcuts import redirect, render, get_object_or_404
from .models import Tags
from triggers.models import Triggers, UserTriggers
from apikey.models import Apikey
from builder.models import Build

# Create your views here.
def tags(request):
    triggers = Triggers.objects.all()
    user_triggers = UserTriggers.objects.all()
    apikey = Apikey.objects.all()
    print(f'UTriggers: {user_triggers}')
    return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
    'apikey': apikey })

def tagGenerate(request):
    if request.method == 'POST':
        try:
            print('POST')
            trigger_for_build = UserTriggers.objects.get(name=request.POST['TriggerNameField'])
            build = Build.objects.get(build_name=trigger_for_build.build)
            print(f'temp: {trigger_for_build.trigger_type}')
            trigger_files = Triggers.objects.get(trigger_type=trigger_for_build.trigger_type)
            print(f'Trigger Files: CSS: {trigger_files.css_file.url} JS: {trigger_files.js_file.url}')
            coder = "<div id='SalersAnt_trigger1'><link rel='stylesheet' href='http://127.0.0.1:8000"+ trigger_files.css_file.url +"'><div id='"+ 'PopUp-SalesAnt' +"' class='modal'><div class='modal-content'><span class='close'>&times;</span>"+ build.build +" </div><script src='http://127.0.0.1:8000"+ trigger_files.js_file.url +"'></script></div>"

            tag = Tags(
                trigger_name = request.POST['TriggerNameField'],
                api_key = request.POST['ApiKeyField'],
                code = coder,
            )
            tag.save()
            print("TagGenerate OK")
            return redirect('/tags')
        except Exception as e:
            print("TagGenerate oops")
            return redirect('/tags')

def tagCodeDelete(request):
    if request.method == 'POST':
        code = get_object_or_404(Tags, trigger_name=request.POST['CodeDeleteValue'])
        code.delete()
        print(f'Code ok')
        return redirect('/tags')

#User Trigger List
def tagsTrigger(request, triggers_selected):
    triggers = Triggers.objects.all()
    user_triggers = UserTriggers.objects.all()
    apikey = Apikey.objects.all()

    slt_based_trg = UserTriggers.objects.filter(trigger_type=triggers_selected) 

    return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
    'apikey': apikey, 'slt_based_trg': slt_based_trg })

#Tag Code
def tagsForTrigger(request, triggers_selected, fortriggers_selected):
    triggers = Triggers.objects.all()
    user_triggers = UserTriggers.objects.all()
    apikey = Apikey.objects.all()

    slt_based_trg = UserTriggers.objects.filter(trigger_type=triggers_selected) 
    try:
        code = Tags.objects.get(trigger_name=fortriggers_selected)
    except Exception as e:
        print(f'Error Code: {e}')
        code = {'code': 'Please Generate'}
    return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
    'apikey': apikey, 'slt_based_trg': slt_based_trg, 'code': code })