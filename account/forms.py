from django import forms

from .models import User


class registrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User with given username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with given email already exists.')
        return email


    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Password do not math ')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user



