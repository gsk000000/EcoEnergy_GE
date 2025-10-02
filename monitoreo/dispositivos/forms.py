from django import forms
from .models import Organization, Device, Category, Zone

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Organization
        fields = ["name", "email", "password"]

    def save(self, commit=True):
        org = super().save(commit=False)
        org.set_password(self.cleaned_data["password"])
        if commit:
            org.save()
        return org
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'category', 'zone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'zone': forms.Select(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }