from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import YNF_Form_List
from django.contrib.auth import authenticate


# Create your views here.
def dc(request):
    if request.user.is_authenticated:
        return redirect('/tags')
    else:
        return redirect('/login')

@csrf_exempt
def dc_ynf(request):
    if request.method == 'POST':
        try:
            if request.POST['s_v'] == '1': #s_v is ApiKey
                new_ynf = YNF_Form_List(
                user = request.POST['u_y'],
                trigger_name = request.POST['ng'],
                collected_email = request.POST['c_e']
                )
                new_ynf.save()
            print('Ok')
        except Exception as e:
            print(f'Error e: {e}')
        
        obj = YNF_Form_List.objects.all()
        print(f'Obj: {obj}')
        return redirect('/')