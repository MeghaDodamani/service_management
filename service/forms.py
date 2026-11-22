from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
    def save(self, commit = True):
        user = super().save(commit=False)
        user.username =self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

        
     