# V 6.1 Documentation
https://docs.djangoproject.com/en/6.1/
https://docs.djangoproject.com/en/6.1/contents/
https://docs.djangoproject.com/en/6.1/topics/templates/
https://docs.djangoproject.com/en/6.1/ref/templates/language/
https://docs.djangoproject.com/en/6.1/ref/templates/builtins/#ref-templates-builtins-tags

# environment setup
Always install Django inside a virtual environment (.venv), never globally. Installing globally can break system tools and causes version conflicts between different projects. [1] 
To address your concern: a .venv does not force you to work inside a subfolder. It is best practice to keep your environment folder separate from your actual source code.
Here is the industry-standard workspace setup for a Django project.
### 1. Recommended Directory Structure
Keep your virtual environment isolated at the root, and place your Django project in its own clean directory.

my-project-wrapper/       <-- Root workspace folder (Open this in VS Code)
├── .venv/                 <-- Isolated environment (Hidden/ignored)
└── src/                   <-- Your actual Django project code
    ├── manage.py
    └── my_django_project/

### 2. Step-by-Step Setup Guide
Step 1: Create the workspace root

mkdir my-project-wrapper
cd my-project-wrapper

Step 2: Create and activate the virtual environment

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

Step 3: Upgrade pip and install Django

pip install --upgrade pip
pip install django

Step 4: Initialize Django inside a src folder
By naming the target directory src, Django puts manage.py inside that folder instead of nesting your project deeply.

django-admin startproject my_django_project src

### 3. Editor Configuration (VS Code Best Practices)
To make your workspace seamless, tell your editor where your environment lives:

* Select Interpreter: Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), search for "Python: Select Interpreter", and choose the path pointing to .venv/bin/python.
* Git Ignore: Create a .gitignore file in your root folder and add .venv/ to it so you never commit your environment to GitHub.

If you want to optimize your environment further, let me know:

* What code editor are you using?
* Do you plan to use Docker later?
* Are you using macOS, Windows, or Linux?

I can provide specific configuration files for your setup.

[1] [https://platzi.com](https://platzi.com/cursos/django/instalacion-de-entornos-virtuales-y-django-en-wind/)
[2] [https://platzi.com](https://platzi.com/cursos/django/instalacion-de-entornos-virtuales-y-django-en-wind/)

# Setup commands
## Create new project
django-admin startproject my_django_project src

## Create new app
cd src
python manage.py startapp <app_name>

# Run DEV Server
python3 src/manage.py runserver

# Django project and app settings
## Settings.py
### add application name to 
INSTALLED_APPS = [
    'challenges', # name defined in challenges/apps.py...

### add templates global path:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"


### add '/static/' global path
STATICFILES_DIRS = [
    BASE_DIR / 'static'
    ]



## src/subapp/urls.py
add this file with:
```python
from django.urls import path
from . import views
# add app_name = "appname" to be able to reverse call the specific url path by path name
app_name = "challenges"
# add path to urlpatterns
urlpatterns = [
    path("", views.index, name="index"),
    path("pol", views.pol, name="pol"),
    path("<str:month>", views.monthly_challenge, name="month_str_path"),
]
```

# src/mainapp/urls.py
include the subapp.urls file in main urlpatterns list:
```python
urlpatterns = [
    path("challenges/", include("challenges.urls")),
    path("admin/", admin.site.urls),
]
```

## views.py
add route functions 
def pol(request):
    return HttpResponse("<h1>Hello. This is POL</h1>")

# VS-CODE CODE EDITOR Settings
## settings.json
```json
{
"files.associations":{
"**/*.html": "html",
"**/templates/**/*.html": "django-html",
"**/templates/**/*": "django-txt",
"**/requirements{/**,*}.{txt,in}": "pip-requirements"
},
"emmet.includeLanguages":{"django-html": "html"}
}
```
