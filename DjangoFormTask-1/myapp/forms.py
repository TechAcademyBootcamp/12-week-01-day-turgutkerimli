from .models import Form, Users
from django import forms

"""
    By changing the name of classes to 'AddressForm'
    you can check the tasks where first and second class refers to the tasks , relatively.
"""

class OldAddressForm(forms.Form):

    email = forms.EmailField(label='Email', required=True, 
            widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'inputEmail4',
                'placeholder': 'Email',
    }))

    password = forms.CharField(label='Password', required=True,
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'inputPassword4',
                'placeholder': 'Password',
    }))

    address = forms.CharField(label='Address', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputAddress',
                'placeholder': 'Address',    
    }))

    address_2 = forms.CharField(label='Address_2', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputAddress2',
                'placeholder': 'Address 2',    
    }))

    city = forms.CharField(label='City', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputCity',
    }))

    state = forms.ChoiceField(label='State', required=True,
            widget=forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputState',
    }))

    zipp = forms.CharField(label='Zip', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputZip',
    }))

    check_me = forms.BooleanField(label='Check me out', initial=False,
            widget=forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'gridCheck',
     }))


class AddressForm(forms.ModelForm):
    user = forms.ChoiceField(label='User', required=True,
            widget=forms.Select(attrs={
                'class': 'form-control',
    }))
    email = forms.EmailField(label='Email', required=True, 
            widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'inputEmail4',
                'placeholder': 'Email',
    }))

    password = forms.CharField(label='Password', required=True,
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'inputPassword4',
                'placeholder': 'Password',
    }))

    address = forms.CharField(label='Address', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputAddress',
                'placeholder': 'Address',    
    }))

    address_2 = forms.CharField(label='Address_2', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputAddress2',
                'placeholder': 'Address 2',    
    }))

    city = forms.CharField(label='City', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputCity',
    }))

    state = forms.ChoiceField(label='State', required=True,
            widget=forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputState',
    }))

    zipp = forms.CharField(label='Zip', required=True,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputZip',
    }))

    check_me = forms.BooleanField(label='Check me out', initial=False,
            widget=forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'gridCheck',
     }))
    class Meta:
        model = Form
        fields = (
              'user',
              'email',
              'password',
              'address',
              'address_2',
              'city',
              'state',
              'zipp',
              'check_me',)