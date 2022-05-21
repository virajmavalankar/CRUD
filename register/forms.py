from django import forms
from register.models import UserModel


class Empforms(forms.ModelForm):
	class Meta:
		model=UserModel
		fields = "__all__"

	