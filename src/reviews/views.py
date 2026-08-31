from django.shortcuts import render, redirect

#V02 WITH ModelForm CLASS
from .forms import ReviewForm

# V01 without ModelForm Class
from .models import Review

# V03 Class View
from django.views import View

# V03
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        render_context = {"form": form}
        return render(request, "reviews/review.html", render_context)

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(f"form.cleaned_data={form.cleaned_data}")
            print(f"form.user_name={form.cleaned_data['user_name']}")
            form.save()

            return redirect("reviews:thank-you")

        # if form is invalid it renders again without deleting data or error messages
        render_context = {"form": form}
        return render(request, "reviews/review.html", render_context)


# Create your views here.
# V01 y V02
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
    #   entered_username = request.POST['username']
        if form.is_valid():
            print(f"form.cleaned_data={form.cleaned_data}")
            print(f"form.user_name={form.cleaned_data['user_name']}")
            # V1 without ModelForm
            # review = Review(
            #                 user_name=form.cleaned_data['user_name'],
            #                 review_text=form.cleaned_data['review_text'],
            #                 rating=form.cleaned_data['rating'])
            # review.save()

            # V2 with ModelForm Class
            form.save()

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

# UPDATE with ModelForm Class
# VALIDATE WITH DJANGO 6.1 DOCS
def review_update(request):
    if request.method == "POST":
        existing_data = Review.objects.get(pk=1) # pending: pk value definition
        form = ReviewForm(request.POST, instance=existing_data)

        if form.is_valid():
            form.save()
            return redirect("reviews:thank-you")

    else:
        form = ReviewForm()

    render_context = {"form": form}
    return render(request, "reviews/review.html", render_context)



def thank_you(request):
    return render(request, "reviews/thank_you.html")
