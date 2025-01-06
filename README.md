<<<<<<< HEAD
# Getting-Started-With-Django-Rest-Framework
=======
## STEPS FOLLOWED

#1 Install django
#2 create dir sample_django_rest
#3 run `django-admin startproject sample_django_rest`
#4 cd sample_django_project\Scripts
#4 run command `activate`
#5 run `python manage.py startapp taskApp`
#6 cd taskApp

#7 create urls.py with below code
```python
    from django.urls import path
    #now import the views.py file into this code
    from . import views

    urlpatterns=[
        path('', views.index)
    ]
```
#8 In views.py inside taskApp, write below code
```python
    from django.shortcuts import render
    from django.http import HttpResponse
    
    
    def index(request):
        return HttpResponse("Hello World!")

```

#9 inside settings.py in main project, add taskApp in *INSTALLED_APPS*

#10 Configure urls.py in main project in below manner:
    - add below line for include()
    `python from django.urls import include`
    - the add url for app inside urlspattern array
    `path('', include('taskApp.urls')),`

#11 In terminal, go to main project folder and run below to start the project
    `python manage.py runserver`

#12 Start https://locahost:8000/ to validate

#13 Stop the app
#14 Run `pip install djangorestframework` to install rest_framework
#15 Go to settings.py and add rest_framework in INSTALLED_APPS

#16 create an API app, python manage.py startapp apis
#17 Go to settings.py and add apis in INSTALLED_APPS
#18 add url as below in sample_django_project/urls.py
```python
    path('', include("apis.urls"))
```
#19 create a customer model, in apis/models.py
```python
    from django.db import models
    class CustomerModel(models.Model):
        name = models.CharField(max_length=200)
        address = models.TextField()

        def __str__(self):
            return self.name
```

#20 create a serializer, apis/serializers.py
```python
    from rest_framework import serializers

    from .models import CustomerModel

    class CustomerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model=CustomerModel
            fields=('name','address')
```
#21 create a viewset, apis/views.py
```python
    from django.shortcuts import render
    from rest_framework import viewsets
    from .serializers import CustomerSerializer
    from .models import CustomerModel

    class CustomerViewSet(viewsets.ModelViewSet):
        queryset = CustomerModel.objects.all()
        serializer_class = CustomerSerializer
```
#22 Define urls and path, apis/urls.py
```python
    from django.urls import include, path
    from rest_framework import routers
    from .views import *

    router = routers.DefaultRouter()

    router.register(r'customer', CustomerViewSet)

    urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls')),
    ]
```
#23 Run `python manage.py makemigrations`
#24 Run `python manage.py migrate`
#25 Run `python manage.py runserver` and validate https://localhost:8000/customer.
>>>>>>> 9324e3a (added all files)
