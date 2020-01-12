from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
	"""Form Review for Movie"""
	class Meta:
		model = Review
		fields = ["text"]