from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import YNF_Form_List
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import DC_mail_user, DC_new_subscriber,YNF_Form_List
from triggers.models import UserTriggers
from user.models import Domains
from apikey.models import Apikey


# Create your views here.
def dc(request):
    if request.user.is_authenticated:
        user_triggers = UserTriggers.objects.filter(user=request.user)
        website = Domains.objects.filter(username=request.user)
        data = YNF_Form_List.objects.filter(user=request.user)
        return render(request, 'dc.html',{'user_triggers': user_triggers, 'website': website,
        'data': data})
    else:
        return redirect('/login')


def dc_mailUsers(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                mailing = DC_mail_user(
                    user = request.user,
                    website = request.POST['mu_website'],
                    trigger_name = request.POST['mu_triggers'],
                    message = request.POST['message'],
                    promo_code = request.POST['promo_code'],
                )
                mailing.save()
            except IntegrityError as e:
                mailing = DC_mail_user.objects.filter(user=request.user, trigger_name = request.POST['mu_triggers'])
                mailing.message = request.POST['message']
                mailing.promo_code = request.POST['promo_code']
                mailing.update()
            except Exception as e:
                print(f'DCMail_Users Error: {e}')

            print(f'List of MU: {DC_mail_user.objects.filter(user=request.user)}')
        return redirect('/dc')

    else:
        return redirect('/login')

def set_subscribers(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                mailing = DC_new_subscriber(
                    user = request.user,
                    website = request.POST['ss_website'],
                    trigger_name = request.POST['ss_triggers'],
                    message = request.POST['message'],
                    promo_code = request.POST['promo_code'],
                )
                mailing.save()
            except IntegrityError as e:
                mailing = DC_new_subscriber.objects.filter(user=request.user, trigger_name = request.POST['ss_triggers'])
                mailing.message = request.POST['message']
                mailing.promo_code = request.POST['promo_code']
                mailing.update()
            except Exception as e:
                print(f'DC_new_subscriber Error: {e}')

            print(f'List of SS: {DC_new_subscriber.objects.filter(user=request.user)}')
        return redirect('/dc')

    else:
        return redirect('/login')

@csrf_exempt
def dc_ynf(request):
    if request.method == 'POST':
        try:
            # if request.POST['s_v'] == '1': #s_v is ApiKey
            #     new_ynf = YNF_Form_List(
            #     user = request.POST['u_y'],
            #     trigger_name = request.POST['ng'],
            #     collected_email = request.POST['c_e']
            #     )
            #     new_ynf.save()

            #New USING APIKEY
            is_key_valid = Apikey.objects.get(user=request.POST['u_y'], key=request.POST['s_v'])
            if is_key_valid is not None:
                new_ynf = YNF_Form_List(
                user = request.POST['u_y'],
                trigger_name = request.POST['ng'],
                # website = request.POST["wsite"],
                collected_email = request.POST['c_e']
                )
                new_ynf.save()
                print('Ok')
            else:
                print('no User with apikey found!')
        except Exception as e:
            print(f'Error e: {e}')
        
        obj = YNF_Form_List.objects.all()
        print(f'Obj: {obj}')
        return redirect('/')