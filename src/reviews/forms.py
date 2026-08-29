from django import forms


class ReviewForm(forms.Form):
    # your_name = forms.CharField(label="Your Name",max_length=100)
    user_name = forms.CharField(
        label="Your Name",
        max_length=10,
        error_messages={
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter name!",
        },
    )
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200
    )
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
