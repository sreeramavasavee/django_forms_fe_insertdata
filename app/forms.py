from django import forms

class course(forms.Form):
    cname=forms.CharField()
    cfee=forms.IntegerField()
    address=forms.CharField()
    