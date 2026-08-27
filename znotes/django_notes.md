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
Class.objeccts.filter(gilter condition) -> QuerySest -> multiple values

### Additional QuerySet methods:
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#django.db.models.query.QuerySet

### Field Lookups
filter conditions -> Field lookups
https://docs.djangoproject.com/en/6.1/ref/models/querysets/#field-lookups

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
