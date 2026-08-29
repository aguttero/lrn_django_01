from django import forms

class ReviewForm(forms.Form):
    # your_name = forms.CharField(label="Your Name",max_length=100)
    user_name = forms.CharField(max_length=10)
