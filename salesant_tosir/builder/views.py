from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Build
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        build = Build.objects.filter(user=request.user)[:5]
        print(f'Build: {build}')
        return render(request, 'index.html', {'build': build})
    else:
        return redirect('/login')

#Save BuildFrame Html code to db
def saveBuildJS(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                build = Build(
                    user = request.user,
                    build_name = request.POST['BuildNameField'],
                    build = request.POST['BuildHtml']
                )
                build.save()
                print(f"Ok {request.POST['BuildNameField']}")
            except IntegrityError as e:
                build_obj = Build.objects.filter(user=request.user, build_name = request.POST['BuildNameField'])
                build_obj.build = request.POST['BuildHtml']
                build_obj.update()
            except Exception as e:
                print(f'Error {e}')
        else:
            print('something went wrong!')
        
        return redirect('/builder/builds')
    else:
        return redirect('/login')

def buildDelete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(f'POST: All Builds of {request.POST["BuildName_del"]}')
            try:
                Build.objects.get(build_name=request.POST['BuildName_del'], user=request.user).delete()
                print(f'Deleted: {request.POST["BuildName_del"]}')
            except:
                print('Not Found!')
        return redirect('/builder/builds')
    else:
        return redirect('/login')

def builder(request):
    if request.user.is_authenticated:
        print(f'USER: {request.user}')
        is_post = False
        if request.method == 'POST':
            try:
                build = Build.objects.get(build_name=request.POST['BuildName'], user=request.user)
                is_post = True
                print(f'build: {build}')
                return render(request, 'builder.html', {'is_post': is_post, 'build': build })
            except Exception as e:
                redirect('/builder/builds')
                print(f"Opps! Build POST, Error: {e}")
        return render(request, 'builder.html', {'is_post': is_post})
    else:
        return redirect('/login')

def allBuilds(request):
    if request.user.is_authenticated:
        build = Build.objects.filter(user=request.user)
        return render(request, 'allbuilds.html', {'build': build})
    else:
        return redirect('/login')

def templates_made(request):
    if request.user.is_authenticated:
        return render(request, 'temps/yn_form.html')
    else:
        return redirect('/login')
