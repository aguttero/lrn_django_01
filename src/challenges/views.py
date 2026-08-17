from django.http import HttpResponse
from django.shortcuts import render

monthly_content_dict = {
    "jan": "Eat no meat",
    "feb": "walk 60 minutes",
    "mar": "study 28 minutes",
    "apr": "go cycling",
    "may": "go trekking",
    "jun": "go swimming",
    "jul": "go yoga",
    "aug": "go dancing",
    "set": "learn django",
    "oct": "go running",
    "nov": "play paddle",
    # "dec": "go sailing",
    "dec": None,
}


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello. This is POL</h1>")


def january(request):
    return HttpResponse("<h1>Hello. This is the January Month page</h1>")

def monthly_challenge(request):
    return HttpResponse
