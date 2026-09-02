from django.shortcuts import redirect, render
from django.views import View

from typing import BinaryIO

# TO SERVE FILES
from django.views.generic import ListView

from .forms import ProfileForm
# Create your views here.

#V03 Model from Models.py
from .models import UserProfile

#V04 CreateView View Class
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# V01 Naive Store File
# V03 we don't need this anymore
def store_file(file:BinaryIO):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            print("storing file...")
            dest.write(chunk)

# V04
# Now can delete form class from V03 - no longer needed
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url =  reverse_lazy("profiles:create")

# TO SERVE FILES
class ListProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles" # default is "object_list"




# V03
class CreateProfileView_v3(View):
    def get(self, request):
        form = ProfileForm() # V02
        return render(request, "profiles/create_profile.html", {"form":form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            print(f"req.FILES= {request.FILES['user_image']}")
            # V02 store_file(request.FILES['user_image'])
            profile = UserProfile(image = request.FILES['user_image'])
            profile.save()
            return redirect("profiles:create")

        return render(request, "profiles/create_profile.html", {"form":submitted_form})



# V01 y V02
class CreateProfileView_v2(View):
    def get(self, request):
        form = ProfileForm() # V02
        return render(request, "profiles/create_profile.html", {"form":form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            print(f"req.FILES= {request.FILES['user_image']}")
            store_file(request.FILES['user_image'])
            return redirect("profiles:create")

        return render(request, "profiles/create_profile.html", {"form":submitted_form})
