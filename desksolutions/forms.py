from django import forms
from .models import OrganizationHead
from django.contrib.auth.forms import UserCreationForm


class OrganizationHeadForm(UserCreationForm):

    # password1 = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput
    # )

    # password2 = forms.CharField(
    #     label="Confirm Password",
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'})
    # )

    class Meta:
        model = OrganizationHead
        fields = ('email', 'title', 'phone', 'description',
                  'url',)
    #     widgets = {
    #         'email': forms.EmailInput(attrs={'class': 'form-control'}),
    #         'title': forms.TextInput(attrs={'class': 'form-control'}),
    #         'phone': forms.TextInput(attrs={'class': 'form-control'}),
    #         'description': forms.Textarea(attrs={'class': 'form-control'}),
    #         'url': forms.TextInput(attrs={'class': 'form-control'}),
    #     }

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user
