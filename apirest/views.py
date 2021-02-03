from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CsvModelForm
from .models import Csv
from django.views.generic import FormView
from django.contrib.auth.models import User
from products.models import Product
from django.core import serializers
import csv
import json


def upload_file_view(request):
    #get file and create object
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        #create a new form to show in error case
        form = CsvModelForm()
        #load the last object create
        obj = Csv.objects.last()
        #load file uploaded
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            #distribute values
            for i, row in enumerate(reader):
                if i != 0:
                    title = row[0]
                    description = row[1]
                    image = row[2]
                    #create object
                    Product.objects.create(
                        title = title,
                        description = description,
                        image = image,
                    )
            return HttpResponseRedirect('/')
    return render(request, 'apirest/upload.html',  {'form':form})

def products(request):
    products = Product.objects.all()
    return render(request, 'apirest/products.html',  {'products':products})

def home(request):
    return render(request, 'apirest/home.html',  {})

def get_products(request):
    products = Product.objects.all()
    if request.method == 'GET':
        return HttpResponse(
        serializers.serialize("json", products),
        content_type="application/json"
        )        
    return render(request, 'apirest/home.html',  {})


def get_product(request, id=None, title=None, description=None, image=None):
    product = {}
    if id != 0:
        product = Product.objects.filter(pk=id)

    if request.method == 'GET':
        print("metod GET")

        return HttpResponse(
        serializers.serialize("json", product),
        content_type="application/json"
        )      
    if request.method == 'DELETE':
        print("metod DELETE")
        if id != 0:
            Product.objects.filter(pk=id).delete()   
    if request.method == 'POST':
        print("metod POST")
        if not id and title and description and image:
            Product.objects.create(
                            title = title,
                            description = description,
                            image = image,
                        )
    if request.method == 'PATCH':
        print("metod PATCH")
        if id and title and description and image:
            Product.objects.create(
                            title = title,
                            description = description,
                            image = image,
                        )
            product, created = Product.objects.get_or_create(pk=id)
            if created:
                product.title = title
                product.description = description
                product.image = image
    return render(request, 'apirest/home.html',  {})


def del_product(request, id=0):
    if id != 0:
        Product.objects.filter(pk=id).delete()   
    return render(request, 'apirest/home.html',  {})