## 1. Instalacion y Creacion del Proyecto

1. Cambiar de directorio en conda

```bash
D:
```

2. Ambiente virtual

```bash
conda create -n django01 python=3.9 # django01 es el nombre del venv
conda activate django01 # activar
conda deactivate django01 # desactivar
```

3. Instalar Django

```bash
pip install django
```

4. Iniciar proyecto

```bash
# Asegurarse estar en el cd deseado
django-admin startproject mysite
# Ruta: http://127.0.0.1:8000/
```

5. Correr server.

```bash
python manage.py runserver
```

6. Iniciar Aplicacion _Polls_.

```bash
python manage.py startapp polls
```

## 2. Archivos:

### mysite/settings.py

```python
# Asegurar que la aplicacion este dentro del archivo setting Root

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ]
```

### polls/models.py

```python
# Se crea la base SQL

from django.db import models

# Cada clase es una tabla
class Question(models.Model):
    # Cada variable es un campo
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Para que al llamar la funcion regrese el contenido, no el objeto
    def __str__(self):
        return self.question_text

    # Un metodo (campo) interno
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Para que al llamar la función regrese el contenido, no el objeto
    def __str__(self):
        return self.choice_text
```

Para actualizar la base SQL utilizar los siguientes comandos:

```bash
# Decirle a DJANGO que modificamos los modelos
python manage.py makemigrations polls
# Para ver el SQL de la migracion 0001
python manage.py sqlmigrate polls 0001
# Crear los modelos en la DB
python manage.py migrate
```

### polls/views.py

```python
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.shortcuts import render # con el paquete render, HttpResponse y loader no son necesarios de importar
from django.http import Http404
from django.shortcuts import get_object_or_404

###########
# Index
###########

# 1er Version Index
    # Simple HttpResponse con texto
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# 2do Version Index
    # 1) Listado de modelos
    # 2) Load template
    # 3) Fill context
    # 4) return an HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

# 3er Version Index:
    # 1) Listado de modelos
    # 2) fill a context,
    # 3) render with the template
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # render(request, template, dictionary)
    return render(request, "polls/index.html", context)

###########
# Detail: Error 404
###########

# 1. Version Error 404
    # raise Http404
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

# 2. Version Error 404
    # get_object_or_404
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

###########
# Results
###########

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

###########
# Vote
###########

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

### Polls/urls.py

```python
# Se agregan las urls que hacen referencia a las vistas creadas

from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

### mysite/urls.py

```python
# Asegurar que que el Root tenga acceso a las url´s de la aplicacion en especifico

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

### polls/templates/polls/---.html

```html
<!-- Se crean los Templates utilizados en las vistas -->

<!-- 
##########    
# INDEX
##########
-->
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}

<!-- 
##########    
# DETAIL
##########
-->
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

### polls/admin.py

```python
# Agregar un menu en el administrador para el modelo

from django.contrib import admin
from .models import Question
admin.site.register(Question)
```

Se necesita crear un superuser

```bash
python manage.py createsuperuser
# user: rafa
# mail: rafa@rafa.com
# psw: 12345
```

## 3. Shell:

Para ingresar datos dentro de los modelos (bases de datos):

1. **Ingresar al shell**

```bash
python manage.py shell
```

2. **Importar insumos**

```python
from polls.models import Choice, Question  # Import the model classes we just wrote.
from django.utils import timezone
current_year = timezone.now().year
```

3. **Metodos**

- Crea objeto dentro de modelo.

```python
q = Question(question_text="What's new?", pub_date=timezone.now())
```

- Guardar

```python
q.save()
```

- Llamar a los objetos

```python
Question.objects.all()
# Respuesta:
#    <QuerySet [<Question: Question object (1)>]>

# Respuesta con la funcion de str dentro del modelo:
#   <QuerySet [<Question: What's up?>]>
```

- Llamar a los objetos del modelo complementario

```python
q.choice_set.all()
```

- Filtrar para obtener **multiples** objetos

```python
Question.objects.filter(id=1)
Question.objects.filter(question_text\_\_startswith="What")
Choice.objects.filter(question**pub_date\_\_year=current_year)
```

- Filtrar para obtener un **unico objeto**, devuelve un error si no encuentra alguno o encuentra muchos

```python
Question.objects.get(id=1)
Question.objects.get(pk=1)
Question.objects.get(pub_date**year=current_year)
```

- Borrar

```python
c = q.choice_set.filter(choice_text\_\_startswith="Just hacking")
c.delete()
```

4. **Atributos/Campos del modelo**

- ID (atributo interno)

```python
q.id
# Respuesta: 1
```

- Campo "question_text"

```python
q.question_text
# Respuesta: "What's new?"
```

- Campo "pub_date"

```python
q.pub_date
# Respuesta: datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)
```

- Cambiar valores de los atributos en el mismo shell donde fue creado (recordar guardar al finalizar)

```python
q.question_text = "What's up?"
```

- Cambiar valores de los atributos tras buscar el valor requerido (recordar guardar al finalizar)

Utilizando un GET

```python
q = Question.objects.get(pk=1)
q.question_text = 'some value'
q.save()
```

Utilizando un Filter y un Update

```python
Question.objects.filter(pk=1).update(question_text='some value')
```

- INSERT al modelo complementario que depende de Question

```python
q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)
```
