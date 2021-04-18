from os import name
import re
from django.shortcuts import redirect, render, get_object_or_404
from .models import Tags
from triggers.models import Triggers, UserTriggers
from apikey.models import Apikey
from builder.models import Build
from django.contrib.auth import authenticate


# Create your views here.
def tags(request):
    if request.user.is_authenticated:
        triggers = Triggers.objects.all()
        user_triggers = UserTriggers.objects.filter(user=request.user)
        apikey = Apikey.objects.filter(user=request.user)
        print(f'UTriggers: {user_triggers}')
        return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
        'apikey': apikey })
    else:
        return redirect('/login')

def tagGenerate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                print('POST')
                trigger_for_build = UserTriggers.objects.get(name=request.POST['TriggerNameField'], user=request.user)
                build = Build.objects.get(build_name=trigger_for_build.build, user=request.user)
                print(f'temp: {trigger_for_build.trigger_type}')
                trigger_files = Triggers.objects.get(trigger_type=trigger_for_build.trigger_type)
                print(f'Trigger Files: CSS: {trigger_files.css_file.url} JS: {trigger_files.js_file.url}')
                coder = "<div id='SalersAnt_trigger1'><link rel='stylesheet' href='http://127.0.0.1:8000"+ trigger_files.css_file.url +"'><div id='"+ 'PopUp-SalesAnt' +"' class='modal'><div class='modal-content'><span class='close'>&times;</span>"+ build.build +" </div><script src='http://127.0.0.1:8000"+ trigger_files.js_file.url +"'></script></div>"

                #REGEX
                regex_pattern = r"TempElementSelected\((.*?)\);"
                coder = re.sub(regex_pattern, '',coder)
                
                regex_pattern = r"contenteditable=\"True\""
                coder = re.sub(regex_pattern, '',coder)

                regex_pattern = r"contenteditable=\"true\""
                coder = re.sub(regex_pattern, '',coder)

                regex_pattern = r"onclick=\"BuildFrameSelected\('BuildFrame'\)\" ondragover=\"onDragOver\(event\);\" ondrop=\"onDrop\(event\);\""
                coder = re.sub(regex_pattern, '',coder)

                tag = Tags(
                    user = request.user,
                    trigger_name = request.POST['TriggerNameField'],
                    api_key = request.POST['ApiKeyField'],
                    code = coder,
                )
                tag.save()
                print("TagGenerate OK")
                return redirect('/tags')
            except Exception as e:
                print(f"TagGenerate oops {e}")
                return redirect('/tags')
    else:
        return redirect('/login')

def tagCodeDelete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            code = get_object_or_404(Tags, trigger_name=request.POST['CodeDeleteValue'])
            if code.user == request.user:
                code.delete()
                print(f'Code ok')
            else:
                print(f'ErrorCodeDelete')
            return redirect('/tags')
    else:
        return redirect('/login')

#User Trigger List
def tagsTrigger(request, triggers_selected):
    if request.user.is_authenticated:
        triggers = Triggers.objects.all()
        user_triggers = UserTriggers.objects.filter(user=request.user)
        apikey = Apikey.objects.filter(user=request.user)

        slt_based_trg = UserTriggers.objects.filter(trigger_type=triggers_selected, user=request.user) 

        return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
        'apikey': apikey, 'slt_based_trg': slt_based_trg })
    else:
        return redirect('/login')

#Tag Code
def tagsForTrigger(request, triggers_selected, fortriggers_selected):
    if request.user.is_authenticated:
        triggers = Triggers.objects.all()
        user_triggers = UserTriggers.objects.filter(user=request.user)
        apikey = Apikey.objects.filter(user=request.user)

        slt_based_trg = UserTriggers.objects.filter(trigger_type=triggers_selected,user=request.user) 
        try:
            code = Tags.objects.get(trigger_name=fortriggers_selected, user=request.user)
        except Exception as e:
            print(f'Error Code: {e}')
            code = {'code': 'Please Generate'}
        return render(request, 'tags.html', { 'triggers': triggers, 'user_triggers': user_triggers, 
        'apikey': apikey, 'slt_based_trg': slt_based_trg, 'code': code })
    else:
        return redirect('/login')