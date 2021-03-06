from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth import authenticate


class FarmerForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model=Farmer
        fields=[ 'username', 'email','dob','is_farmer','aadhar_no','pan_no','password', 'confirm_password']

        labels = {
        "dob": "Date Of Birth",
        'is_farmer': 'Register as a farmer',
        'aadhar_no':'Enter Your Aadhar card number',
        'pan_no':'Enter  your PAN number',
        }
    def clean(self):
        cleaned_data = super(FarmerForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

    def __init__(self,*args,**kwargs):
        super(FarmerForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['dob'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['aadhar_no'].widget.attrs['class'] = 'form-control'
        self.fields['aadhar_no'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['aadhar_no'].widget.attrs['placeholder'] = 'Aadhar-no'
        self.fields['pan_no'].widget.attrs['class'] = 'form-control'
        self.fields['pan_no'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['pan_no'].widget.attrs['placeholder'] = 'Pan Number'
        self.fields['is_farmer'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_farmer'].widget.attrs['id'] = 'inlineRadio2'


class BuyerForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model=Buyer
        fields=[ 'username', 'email','dob','is_farmer','aadhar_no','pan_no','password', 'confirm_password']

        labels = {
        "dob": "Date Of Birth",
        'is_farmer': 'Register as a farmer',
        'aadhar_no':'Enter Your Aadhar card number',
        'pan_no':'Enter Your PAN card number',
        }
    def clean(self):
        cleaned_data = super(BuyerForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

    def __init__(self,*args,**kwargs):
        super(BuyerForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class AccountAuthenticationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control','id':'submit','placeholder':"Username"}))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'id':'exampleInputPassword1','class':'form-control','placeholder':'Password'}),
    )
    class Meta:
        model = Account
        fields = ('username', 'password')


    def clean(self):
        print(self.cleaned_data['username'])
        print(self.cleaned_data['password'])
        if self.is_valid():
            print("here")
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            print(password)
            print(authenticate(password=password,username=username))
            if not authenticate(password=password,username=username):
                raise forms.ValidationError("Invalid login")

    def __init__(self,*args,**kwargs):
        super(AccountAuthenticationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self,*args,**kwargs):
        super(CartAddProductForm,self).__init__(*args,**kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'btn btn-warning'
        self.fields['update'].widget.attrs['class'] = 'btn btn-warning'

class CropForm(ModelForm):
    class Meta:
        model = Crops
        fields= [ 'name', 'c_type','price','photo','quantity']

        labels = {
                  'name':'Name of Your crop',
                  'c_type':'Variety of your crop',
                  'price':'Price per quintal you want to sell',
                  'quantity':'Quintals of Crop for sale',
                  'photo':'Image of the ready crop (Optional)',
                  }

        
    def __init__(self,*args,**kwargs):
        super(CropForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['id'] = 'exampleInputEmail1'
        self.fields['name'].widget.attrs['placeholder'] = 'Crop name'
        self.fields['c_type'].widget.attrs['class'] = 'form-control'
        self.fields['c_type'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['c_type'].widget.attrs['placeholder'] = 'Category'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['id'] = 'exampleInputPassword1'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Quantity'
        # self.fields['photo'].widget.attrs['class'] = 'btn btn-primary'


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']

    def __init__(self,*args,**kwargs):
        super(OrderCreateForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['postal_code'].widget.attrs['class'] = 'form-control'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Postal_Code'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'