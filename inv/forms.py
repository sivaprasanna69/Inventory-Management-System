from django import forms
from . models import *


class LaptopForm(forms.ModelForm):
	class Meta:
		model = laptop
		fields = ('typee','price','status','issues')

class DesktopForm(forms.ModelForm):
	class Meta:
		model = Desktop
		fields = '__all__'

class MobileForm(forms.ModelForm):
	class Meta:
		model = Mobile
		fields = '__all__'