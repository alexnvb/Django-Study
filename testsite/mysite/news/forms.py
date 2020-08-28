from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Theme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Body', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='User Name', help_text='input your name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Name title', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label='Public', initial=True)
#     category = forms.ModelChoiceField(empty_label='Select Category',label='Category',queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Name must not start number')
        return title
