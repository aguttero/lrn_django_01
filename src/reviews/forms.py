from django import forms

# V2 from models.py form definition
from .models import Review

# V1 initial manual for definition
# class ReviewForm(forms.Form):
#     # your_name = forms.CharField(label="Your Name",max_length=100)
#     user_name = forms.CharField(
#         label="Your Name",
#         max_length=10,
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter name!",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200
#     )
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# V2 Definition based in models.py
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # define fielsds to include in form from model fields: list
        fields = "__all__"
        # can use exclude: list to exclude some form all
        # exclude = ['internal_comment']
        # For additional configuration for the field parameters:
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }
        max_length = {}
