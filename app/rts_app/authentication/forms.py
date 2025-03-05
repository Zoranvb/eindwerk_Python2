from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_password2(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords must match")
        return self.cleaned_data.get("password2")
