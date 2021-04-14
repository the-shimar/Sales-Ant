from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Build

# Create your views here.
def index(request):
    build = Build.objects.all()[:5]
    print(f'Build: {build}')
    return render(request, 'index.html', {'build': build})

#Save BuildFrame Html code to db
def saveBuildJS(request):
    if request.method == 'POST':
        build = Build(
            user = request.user,
            build_name = request.POST['BuildNameField'],
            build = request.POST['BuildHtml']
        )
        build.save()
        print(f"Ok {request.POST['BuildNameField']}")
    else:
        print('something went wrong!')
    
    return redirect('/builder/builds')

def buildDelete(request):
    if request.method == 'POST':
        print(f'POST: All Builds of {request.POST["BuildName"]}')
        try:
            Build.objects.get(build_name=request.POST['BuildName']).delete()
            print(f'Deleted: {request.POST["BuildName"]}')
        except:
            print('Not Found!')
    return redirect('/builder/builds')

def builder(request):
    is_post = False
    if request.method == 'POST':
        try:
            build = Build.objects.get(build_name=request.POST['BuildName'])
            is_post = True
            print(f'build: {build}')
            return render(request, 'builder.html', {'is_post': is_post, 'build': build })
        except Exception as e:
            redirect('/builder/builds')
            print(f"Opps! Build POST, Error: {e}")
    return render(request, 'builder.html', {'is_post': is_post})

def allBuilds(request):
    build = Build.objects.all()
    return render(request, 'allbuilds.html', {'build': build})

def templates_made(request):
    return render(request, 'temps/yn_form.html')
