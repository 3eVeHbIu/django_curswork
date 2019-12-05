from django.shortcuts import render, redirect
from .models import News, Themes
from .forms import UserForm, NewsForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

'''
БАГИ:
    Ограничить доступ к редактированию все пользователям кроме создателя
    Сейчас можно загружать фото только с название не состоящим из цифр, иначе происходит ошибка
ИДЕИ:
    Реализовать активацию аккаунта по почте
'''


def index(request):
    news = News.objects.all()
    themes = Themes.objects.all()
    context = {'news': news, 'themes': themes}
    if request.user.is_authenticated:
        paginator = Paginator(news, 5)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'page': page, 'news': page.object_list, 'themes': themes}
    return render(request, 'NewsFeed/index.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
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


@login_required
def create_post(request):
    themes = Themes.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            news.creator = request.user
            news.save()
            return redirect('index')
        else:
            errors = UserForm.errors
            context = {'form': form, 'errors': errors, 'themes': themes}
            return render(request, 'NewsFeed/create.html', context)
    else:
        form = NewsForm()
        context = {'form': form, 'themes': themes}
        return render(request, 'NewsFeed/create.html', context)


@login_required
def edit(request, news_id):
    themes = Themes.objects.all()
    news = News.objects.get(pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            if form.has_changed():
                form.save()
            return redirect('index')
        else:
            errors = UserForm.errors
            context = {'form': form, 'errors': errors,
                       'themes': themes, 'id': news_id}
            return render(request, 'NewsFeed/edit.html', context)
    else:
        form = NewsForm(instance=news)
        context = {'form': form, 'themes': themes, 'id': news_id}
        return render(request, 'NewsFeed/edit.html', context)


@login_required
def by_theme(request, theme_id):
    themes = Themes.objects.all()
    news = News.objects.filter(subjects=theme_id)
    context = {'news': news, 'themes': themes}
    if request.user.is_authenticated:
        paginator = Paginator(news, 5)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'page': page, 'news': page.object_list, 'themes': themes}
    return render(request, 'NewsFeed/index.html', context)
