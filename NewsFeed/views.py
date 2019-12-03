from django.shortcuts import render, redirect
from .models import News
from .forms import UserForm, NewsForm
from django.contrib.auth import authenticate, login


def index(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'NewsFeed/index.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                # return redirect('login') # Доделать активацию по почте
                login(request, user)
                return redirect('index')
            else:
                errors = UserForm.errors
                context = {'form': form, 'errors': errors}
                return render(request, 'registration/registration.html', context)
        else:
            form = UserForm()
            context = {'form': form}
            return render(request, 'registration/registration.html', context)
