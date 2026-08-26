from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
def pol(request):
    return HttpResponse("<h1>Hello. This is app CHALLENGES POL</h1>")


# WITH TEMPLATE RENDER
def index(request):
    month_list = list(monthly_content_dict.keys())
    context_dict = {
        "month_list": month_list,
    }
    return render(request, "challenges/index.html", context_dict)


# filter by int and redirect
# HARDCODED REDIRECT and REVERSE REDIRECT
def monthly_challenge_by_number(request, month: int):
    months_list1 = list(monthly_content_dict.keys())

    print(f"month value={month} type={type(month)}")
    print(f"months_list1= {months_list1}")

    # VALIDATE input is whitin index list
    if month > len(months_list1):
        raise Http404("ZAG 404: Index out of range")

    # HARDCODED REDIRECT
    # redirect_month = months_list1[month-1]
    # return redirect("/challenges/"+redirect_month)

    # REVERSE REDIRECT (NAME in urls.py name attribute)
    redirect_month = months_list1[month - 1]
    # OLD WAY using reverse
    # from django.ulrs import reverse
    # redirect_path = reverse("month-challenge", args=[redirect_month])
    return redirect("month_str_path", redirect_month)


# V1 without RENDER
# def monthly_challenge(request, month: str):
#     challenge_text = monthly_content_dict.get(month,None)
#     print (f"challenge_text= {challenge_text}")
#     if month == "badurl":
#         raise Http404("sample 404 response")
#     if challenge_text:
#         return HttpResponse(f"Challenge for {month}: {challenge_text}")
#     else:
#         raise Http404("ZAG 404: Month not found")


# V2 WITH RENDER
def monthly_challenge(request, month: str):
    challenge_text = monthly_content_dict.get(month, None)
    print(f"challenge_text= {challenge_text}")
    if month == "badurl":
        raise Http404("sample 404 response")
    # if challenge_text or not challenge_text: # para que aparezca el None en el e render del template
    if challenge_text:
        context_dict = {"challenge_item": challenge_text, "selected_month": month}
        return render(
            request=request,
            template_name="challenges/challenge_item.html",
            context=context_dict,
        )
    else:
        raise Http404("ZAG 404: Month not found")
