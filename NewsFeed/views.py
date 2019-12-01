from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'NewsFeed/index.html',)


def registration(request):
    # if user auntificated

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # return redirect('login')
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
