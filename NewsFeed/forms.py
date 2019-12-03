from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators
from captcha.fields import CaptchaField
from .models import News, Themes


class UserForm(forms.ModelForm):
    # Вещаются на label  как повесить на input?
    error_css_class = 'is-invalid'
    required_css_class = 'is-valid'
    ###
    field_order = ('email', 'username',
                   'first_name', 'last_name', 'password1', 'password2')
    username = forms.CharField(label='Имя пользователя',
                               min_length=4,
                               widget=forms.widgets.TextInput(attrs={'placeholder': 'Ivan', 'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             widget=forms.widgets.EmailInput(attrs={'placeholder': 'ivan@mail.com',
                                                                    'class': 'form-control'}))
    first_name = forms.CharField(label='Имя',
                                 min_length=2,
                                 validators=[validators.RegexValidator(
                                     regex='^([A-zА-я])+$')],
                                 error_messages={
                                     'invalid': 'Имя может содержать только Латиницу или Кириллицу'},
                                 widget=forms.widgets.TextInput(attrs={'placeholder': 'Иван', 'class': 'form-control'}),)
    last_name = forms.CharField(label='Фамилия',
                                min_length=2,
                                validators=[validators.RegexValidator(
                                    regex='^([A-zА-я])+$')],
                                error_messages={
                                    'invalid': 'Фамилия может содержать только Латиницу или Кириллицу'},
                                widget=forms.widgets.TextInput(attrs={'placeholder': 'Иванов', 'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                min_length=6,
                                widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторить пароль',
                                min_length=6,
                                widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="Введите текст с картинки",
                           error_messages={'invalid': 'Неправильный текст'})

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'password1', 'password2',)

    def clean(self):
        super().clean()
        errors = {}
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            errors['password1'] = ValidationError('Пароли не совпадают')
        if User.objects.filter(email=self.cleaned_data['email']):
            errors['email'] = ValidationError('Email уже занят')
        if User.objects.filter(username=self.cleaned_data['username']):
            errors['email'] = ValidationError(
                'Такое имя пользователя уже зарегистрировано')
        if errors:
            raise ValidationError(errors)


class NewsForm(forms.ModelForm):
    # Вещаются на label  как повесить на input?
    error_css_class = 'is-invalid'
    required_css_class = 'is-valid'
    ###
    field_order = ('headline', 'subjects', 'description', 'image',)
    headline = forms.CharField(label='Название статьи',
                               widget=forms.widgets.TextInput(attrs={'placeholder': 'Заголовок', 'class': 'form-control'}))
    subjects = forms.ModelMultipleChoiceField(label='Выберете тематику',
                                              queryset=Themes.objects.all(),
                                              widget=forms.widgets.SelectMultiple(attrs={'class': 'custom-select'}))
    description = forms.CharField(label='Текст статьи',
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Изображение',)

    class Meta:
        model = News
        fields = ('headline', 'subjects', 'description', 'image',)
