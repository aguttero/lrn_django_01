from typing import override

from django.shortcuts import render, redirect

#V02 WITH ModelForm CLASS
from .forms import ReviewForm

# V01 without ModelForm Class
from .models import Review

# V03 Class + Std View
from django.views import View

# V04 Class + Templage View
# from django.views.generic.base import TemplateView # Udemy
from django.views.generic import TemplateView, ListView, DetailView # DJ 6.1 docs

#V05
from django.views.generic.edit import FormView

# V03
class ReviewView_v3(View):
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

            return redirect("reviews:thank_you")

        # if form is invalid it renders again without deleting data or error messages
        render_context = {"form": form}
        return render(request, "reviews/review.html", render_context)

#V05 FormView
class ReviewView(FormView):
    # GET
    form_class = ReviewForm
    template_name = "reviews/review.html"
    # With the upper three lines the get method is covered

    # POST
    # redirect("reviews:thank_you")
    success_url = "thankyou"




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

            return redirect("reviews:thank_you")

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
            return redirect("reviews:thank_you")

    else:
        form = ReviewForm()

    render_context = {"form": form}
    return render(request, "reviews/review.html", render_context)


#V1 Std render return
def thank_you(request):
    return render(request, "reviews/thank_you.html")

#v3 std view return
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

#v4 Template view return
class ThankYouView(TemplateView):
   template_name = "reviews/thank_you.html"
# See s154 to add context data to template

# Review List with Class Template View and context data method
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# Review List with Class List View
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # context_object_name = "reviews" # to convert 'object_list' to 'reviews' context var name -> template

    # optional
    # To filter the list sent to template:
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=4)
        return data

class ReviewItemView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # context_object_name = "review"

    # def get_queryset(self,review_id):
    #      base_query = super().get_queryset()
    #      data = base_query.objects.get(id=review_id)
    #      return data
