from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction
class RegisterForm(UserCreationForm):
 email=forms.EmailField(required=True)
 class Meta: model=User; fields=("username","email","password1","password2")
 def save(self,commit=True):
  user=super().save(commit=False); user.email=self.cleaned_data["email"]
  if commit:user.save()
  return user
class TransactionForm(forms.ModelForm):
 class Meta:
  model=Transaction; fields=("amount","description","category","date")
  widgets={"date":forms.DateInput(attrs={"type":"date"})}
 def clean_amount(self):
  amount=self.cleaned_data["amount"]
  if amount<=0: raise forms.ValidationError("Amount must be greater than zero.")
  return amount
