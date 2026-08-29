from django.shortcuts import render, redirect

#V02 WITH FOrM CLASS
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
    #   entered_username = request.POST['username']
        if form.is_valid():
            print(f"form.cleaned_data={form.cleaned_data}")
            print(f"form.user_name={form.cleaned_data['user_name']}")
            return redirect("reviews:thank-you")

    # if GET request or form.post is not valid:
    # form = ReviewForm()
    #
    # else GET request: Resetted empty form
    else:
        form = ReviewForm()

    # if form is invalid it renders again without deleting data or error messages
    render_context = {"form": form}
    return render(request, "reviews/review.html", render_context)

def thank_you(request):
    return render(request, "reviews/thank_you.html")
