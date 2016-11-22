from django import forms
from .models import Profile

class Post_data(forms.ModelForm):

	name = forms.CharField(label="name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	email = forms.CharField(label="Email", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
	institute = forms.CharField(label="Institute", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	areas_of_interest = forms.CharField(label="Areas Of Interest", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
	skype_id = forms.CharField(label="Skype ID", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))

	class Meta:
		model = Profile
		fields = ('name', 'email', 'institute', 'areas_of_interest', 'upload_cv', 'skype_id')
