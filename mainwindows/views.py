from django.shortcuts import render, redirect
from .models import stati
from .forms import StatiForm
def Kus(request):
    return render(request,'mainwindows/base.html' )
def about(request):
    return render(request, 'mainwindows/about-me.html')
def stats(request):
    stat = stati.objects.all() #[:5]
    return render(request, 'mainwindows/stati.html',{"stat":stat})

def create(request):
    form = StatiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    form = StatiForm()
    context = {
        'form':form
    }

    return render(request,'mainwindows/create.html', context)