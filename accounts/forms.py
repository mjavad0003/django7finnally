from django import forms

class SignUpForm(forms.Form):
    username= forms.CharField()
    email= forms.EmailField()
    password= forms.CharField()


class LoginForm(forms.Form):
    username= forms.CharField()
    password= forms.CharField()
