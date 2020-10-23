from django import forms
from moon.models.order import Coupon

class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = ['code']

class RawCouponForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Facultatif.."}))
