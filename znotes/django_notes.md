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

## delete/rename app
if app is empty just delete it or move it
in not empty check:
* settings.py
* urls.py
* update subapp/apps.py
* udpate imports reference in other files
* update urls.py

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


### Set files MEDIA ROOT path
MEDIA_ROOT = BASE_DIR / "uploads"

### Set URL path for client downloads - ZAG Pending validation of Best PRactice for Django v6
MEDIA_URL = "/user-media/" # this is the virtual url path shown to the client browser
Edit Global url.py:
from django.conf.urls.static import static
from django.conf import settings
ulrpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


### Set Time Zone
While you’re editing mysite/settings.py, set TIME_ZONE to your time zone.

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
# SQL Database
## Sqlite
db.slqite3 file auto created in src/db.sqlite3
## When to use sqlite?
https://sqlite.org/whentouse.html
Generally speaking, any site that gets fewer than 100K hits/day should work fine with SQLite. The 100K hits/day figure is a conservative estimate, not a hard upper bound. SQLite has been demonstrated to work with 10 times that amount of traffic.

## Django Manage.py documentation
https://docs.djangoproject.com/en/6.1/ref/django-admin/

## Django DB setup
https://docs.djangoproject.com/en/6.1/intro/tutorial02/

1. run initial django db table setup:
cd src [ZAG test ok in dev: run from root project folder and ] python3 src/manage.py migrate
run: python3 manage.py migrate

2. populate src/subapp/models.py
3. cd src [ZAG test ok in dev: run from root project folder and ] python3 src/manage.py makemigrations
4. run: python3 manage.py makemigrations [optional subapp name]
4.1 Optional: To print to screen the sql to be generated: (does not affect DB)
  run: python3 manage.py sqlmigrate subapp 0001
4.2 Optional: run: python3 manage.py check
this checks for any problems in your project without making migrations or touching the database.
5. To execute command in DB
  run: python3 manage.py migrate

### Migrations
Migrations let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data.

#### three-step guide to making model changes:

* Change your models (in models.py).
* Run python manage.py makemigrations to create migrations for those changes.
* Run python manage.py migrate to apply those changes to the database.

#### Migration that involves normalization
PENDING.... on how to resolve

### explore with django python shell
* run: python manage.py shell

## DB Rollback
### Rollback to Zero
python manage.py migrate <app_name> zero

### Complete delete DB
sqlite:
Manually delete your db.sqlite3 file from the project root

delete local migration files:
Delete all files inside your app's migrations/ folder except for the __init__.py file.
delete __pycache--

### Rollback one step (undo last migration)
1.Target the name of the migration before your mistake.
run: python manage.py migrate <app_name> <previous_migration_name>

Tip: If you want to undo the very first migration (0001_initial), run python manage.py migrate <app_name> zero.

2. Delete the bad migration file: Manually delete the specific 000X_...py file from your app's migrations/ folder.

3. Remake the migration: Fix your models.py file, then generate a clean file.
run: python manage.py makemigrations
  python manage.py migrate

### Rollback to zero keeping django internal tables
If you want to clear out your app's custom tables but keep Django's built-in user and admin tables, use this workflow:
```bash
# 1. Clear the app's database tables
python manage.py migrate <app_name> zero

# 2. Re-generate the initial migration file
python manage.py makemigrations

# 3. Apply the fresh migration
python manage.py migrate
```

## database CRUD api
see playin with the api
https://docs.djangoproject.com/en/6.1/intro/tutorial02/
run: python3 src/manage.py shell
### write:
>>> from book_outlet.models import Book
>>> harry_potter = Book(title="Harry Potter book 1",rating=5)
>>> harry_potter.save() -> write record to DB

### read:
>>> Book.objects.all()

## Field validators
https://docs.djangoproject.com/en/6.1/ref/validators/
https://docs.djangoproject.com/en/6.1/ref/validators/#how-validators-are-run

## Python crud
### through var
Create:
new_item = Class(values)
new_item.save()
Select, update, delete:
item_var = Class.objects.all()[index]
item_var.save() -> upsert
item.delete()

### directly
Class.objects.create(values) 

## Queries:
https://docs.djangoproject.com/en/6.1/topics/db/queries/

### QuerySet method get()
Class.objects.get(filter condition.. ej: id=3) -> one value

### QuerySet method filter()
Class.objeccts.filter(filter condition) -> QuerySest -> multiple values

### Additional QuerySet methods:
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#django.db.models.query.QuerySet

### Field Lookups
filter conditions -> Field lookups
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#field-lookups

### Query related data (table relationship)
https://docs.djangoproject.com/en/6.1/topics/db/queries/
https://docs.djangoproject.com/en/6.1/topics/db/queries/#related-objects
books_by_rowling = Book.objects.filter(author__last_name="Rowling")
author__ double underscore indicates relationship field
Additional filter modifier with __
books_by_rowling = Book.objects.filter(author__last_name__contains="wling")

### Inverse Query RelatedClass_Set - s107
jkr = Author.objects.get(first_name="JK")
queryset = jkr.book_set.all()) -> query set of books related to given author

#### Optional use related_name="books" in Foreign Key definition - s107
jkr = Author.objects.get(first_name="JK")
queryset = jkr.books.all() -> query set of books related

### One to one relations s109
address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
Dont need to use related_name. Django does it automatically in 1-to-1 relationships
author.address.street
The inverse also works automatically
Address.objects.all()[0].auhtor.first_na,e

### Many to Many Relations s112
new_country = Country(name="Chile", code="CL")
new_country.save()
mybook.published_countries.add(new_country)
Query:
mybook.published_countries.filter(code="CL")

Inverse:
chile = Country.objects.all()[0]
chile.book_set.all() -> Query set
Can add a related name books to the relationship attributes to use chile.books.all()

### Circular, Lazy and related to other app relationships
s115



### Q Query constructor
Complex lookups with Q objects
from django.db.models import Q
| -> OR
, -> and
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(author="JKRowling"))
https://docs.djangoproject.com/en/6.1/topics/db/queries/#s-complex-lookups-with-q-objects
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#q-objects

### Q Query equivalent AND, OR  XOR
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#operators-that-return-new-querysets


### Query Performance
Cache > store a Query in a variable before printing or doing anythong with it
This activates Django Cache.
See Udemy s85 for explanation

### DB Bulk operations
https://docs.djangoproject.com/en/6.1/topics/db/queries/#deleting-objects
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#delete
https://docs.djangoproject.com/en/6.1/topics/db/queries/#updating-multiple-objects-at-once
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#bulk-create
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#bulk-update

### Aggregation
https://docs.djangoproject.com/en/6.1/topics/db/aggregation/#

## Relationships
Needs to be planed before hand

# Forms
https://docs.djangoproject.com/en/6.1/topics/forms/
https://docs.djangoproject.com/en/6.1/intro/tutorial04/

## ModelForms
https://docs.djangoproject.com/en/6.1/topics/forms/modelforms/


## FormViews
https://docs.djangoproject.com/en/6.1/topics/class-based-views/generic-editing/#:~:text=FormView%3A
https://docs.djangoproject.com/en/6.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView



### reverse_lazy() for URL redirect in FormView

Since success_url is a class attribute, it gets evaluated when the class is defined (at import time) — before Django's URL resolver (urls.py) has necessarily finished loading. So you can't use reverse() directly here, because it would try to resolve the URL too early and could throw an error.

That's what reverse_lazy() is for — it returns a lazy object that only gets evaluated when it's actually used (i.e., when Django needs the URL string), not when the class is defined.
https://docs.djangoproject.com/en/6.1/ref/urlresolvers/#django.urls.reverse_lazy

```python
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact-thanks")  # name of a URL pattern in subapp/urls.py
```

### reverse dynamic for ULR redirect in FormView 

get_success_url() — when you need it dynamic

Sometimes the destination URL depends on the object being created/updated (e.g., "redirect to this new object's detail page"). For that, override the get_success_url() method instead of the class attribute — methods are evaluated at request time, so reverse() (not reverse_lazy) works fine here:
```python
from django.urls import reverse

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm

    def get_success_url(self):
        return reverse("contact-thanks")
    # OR with dynamic data e.g. redirecting to a related object's page     
    def get_success_url(self):
        return reverse("thing-detail", kwargs={"pk": self.object.pk})
```

#### Rule of thumb for reverse_lazy or get_success_url
* Static, unchanging destination → success_url = reverse_lazy("url-name")
* Destination depends on runtime data (form input, created object, request user, etc.) → override get_success_url() with reverse()

Either way, the key habit is: never write raw URL strings in your views — always reference URL names and let reverse/reverse_lazy build the path for you. That's the Django-idiomatic way to keep your views decoupled from your URL structure.

### CreateView -> Form
https://docs.djangoproject.com/en/6.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
Avoids creating form class in forms.py
based on Models.py Class to create a view to gather data
View Session 161


# Class-based views
https://www.udemy.com/course/python-django-the-practical-guide/learn/lecture/26399256#overview

# File Uploads & Storage
https://docs.djangoproject.com/en/6.1/topics/http/file-uploads/
ZAG: Validate with 6.1 documentation the secure way to upload and validate

## File download validate with 6.1 the way to handle download
* s171 y 172 in Udemy
### Claude: 1. Static files (CSS, JS, images baked into your app)
Never serve these through a Django view in production. Django's own docs are blunt about this: Django isn't a static file server, and hand-rolling it is "grossly inefficient and probably insecure, so it is unsuitable for production." 
Django
* In development, django.contrib.staticfiles handles this automatically via runserver when DEBUG = True — you don't need to do anything special.

* In production, let something else serve them entirely:

A reverse proxy (Nginx/Apache) serving straight from STATIC_ROOT, or
A CDN / object storage (S3, Cloudflare R2, etc.) via django-storages, or
WhiteNoise (whitenoise.middleware.WhiteNoiseMiddleware) if you want Python to serve them but efficiently, with caching headers and compression handled for you — popular for small-to-medium apps on platforms like Heroku/Render.

Run python manage.py collectstatic to gather everything into STATIC_ROOT for deployment.

### Claude: 2. User-uploaded media files (things saved via FileField/ImageField)
Same story — in dev, Django can serve them via django.views.static.serve() (wired up automatically if you add this to urls.py):
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
In production, again — offload to Nginx/Apache or object storage (S3 is the most common pattern via django-storages), not Django.

### 3. Dynamic / protected file downloads (the case where Django should serve it)
This is the one case where serving a file through a Django view is legitimate even in production — e.g., a PDF invoice that only the logged-in owner should download, or a generated report. Here you use FileResponse:
```python
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from pathlib import Path

@login_required
def download_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    file_path = Path(invoice.file.path)
    if not file_path.exists():
        raise Http404

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=file_path.name,
    )
    ```
### Key points for your junior-dev mental model:

* FileResponse streams the file in chunks instead of loading it all into memory — important for large files.
* as_attachment=True forces a download dialog instead of rendering inline in the browser.
* Because this goes through a view, you get to add authorization checks (login_required, ownership checks, etc.) — that's the whole reason you're not just linking directly to MEDIA_URL.

#### Best practice at scale: even for protected downloads, don't make Django stream the actual bytes in production — it's slow and ties up a worker process for the whole transfer. Instead:
* Nginx: use X-Accel-Redirect — Django checks auth, then tells Nginx "you serve this file," and Nginx does the actual byte-shoveling.
* S3/object storage: generate a short-lived pre-signed URL and redirect the user to it. Django never touches the file bytes at all.

#### Quick decision table
| File type | Dev | Production |
|---|---|---|
| Static assets (CSS/JS) | `runserver` auto | Nginx / CDN / WhiteNoise |
| Public media uploads | `static()` helper | Nginx / S3 direct |
| Protected/dynamic downloads | `FileResponse` in a view | `FileResponse` (small files) or `X-Accel-Redirect` / pre-signed S3 URL (better) |

The pattern to internalize: Django's job is to decide whether you're allowed to have the file. Someone else's job is to actually push the bytes over the wire.

# Sessions
http://docs.djangoproject.com/en/6.1/topics/http/sessions/
## settings.py
Validate that is incliuded in 
MIDDLEWARE -> django.contrib.sessions.middleware.SessionMiddleware
INSTALLED_APPS -> 'django.contrib.sessions', 

### Session Cokkie 
* Default is set to 2 Weeks
* To modify add SESSION_COOKIE_AGE = int:seconds 

# Admin Module
## Setup
https://docs.djangoproject.com/en/6.1/intro/tutorial02/#introducing-the-django-admin
python manage.py createsuperuser
usr: admin
eml: test@test.com
pwd: pwd

## add subapps to admin
https://docs.djangoproject.com/en/6.1/intro/tutorial02/
in subapp/admin.py
from django.contrib import admin
from .models import subapp_Class
admin.site.register(subapp_class)

## Configuring Model fields and admin settings
see s99 and s100 in Udemy Django
trick
class subappClassAdmin(admin.ModelAdmin):
