from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.widgets.TextInput(attrs={'placeholder': 'Ivan', 'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             widget=forms.widgets.EmailInput(attrs={'placeholder': 'ivan@mail.com',
                                                                    'class': 'form-control'}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.widgets.TextInput(attrs={'placeholder': 'Иван', 'class': 'form-control'}),)
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.widgets.TextInput(attrs={'placeholder': 'Иванов', 'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторить пароль',
                                widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1',
                  'password2', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_fild(self):
        pass
