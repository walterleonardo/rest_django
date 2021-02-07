from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CsvModelForm
from .models import Csv
from django.views.generic import FormView
from django.contrib.auth.models import User
from products.models import Product
from django.core import serializers
import csv
import requests
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt



def is_url_image(image_url):
	image_formats = ("image/png", "image/jpeg", "image/jpg")
	r = requests.head(image_url)
	if r.headers["content-type"] in image_formats:
		return True
	return False

def upload_file_view(request, *args, **kwargs):
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
                    try:
                        title = row[0] or 'title'
                        description = row[1] or 'description'
                        if is_url_image(row[2]):
                            image = row[2]
                        else:
                            image = '/static/no_image.png'       
                    except:
                        continue
                    #create object
                    Product.objects.create(
                        title = title,
                        description = description,
                        image = image,
                    )
            return HttpResponseRedirect('/')
    return render(request, 'apirest/upload.html',  {'form':form})

def products(request, *args, **kwargs):
    products = Product.objects.all().order_by('-id')
    return render(request, 'apirest/show_products.html',  {'products':products})

def home(request):
    return render(request, 'apirest/home.html',  {})

@csrf_exempt
def get_product(request, *args, **kwargs):
    product = []
    id = request.GET.get('id',None)
    title = request.POST.get('title',None)
    description = request.POST.get('description',None)
    image = request.POST.get('image',None)
    if request.method == 'GET' and id:
        product = Product.objects.filter(pk=id)
        if not product:
            product = []
        return HttpResponse(serializers.serialize("json", product),content_type="application/json")  
    if request.method == 'GET':
        product = Product.objects.all()
        if not product:
            product = []
        return HttpResponse(serializers.serialize("json", product),content_type="application/json")      
    if request.method == 'DELETE':
        if id:
            Product.objects.filter(pk=id).delete()   
            return HttpResponse([{'Product deleted':id}],content_type="application/json")
        return HttpResponse([{'Required fields':'id'}],content_type="application/json")

    if request.method == 'POST':
        if not id and title:
            product = Product.objects.create(
                            title = title,
                            description = description,
                            image = image,
                        )
            product_created = Product.objects.filter(pk=product.pk)
            return HttpResponse(serializers.serialize("json", product_created),content_type="application/json")    
        else:
            product = [{'Required fields':'title'}]
            return HttpResponse(product,content_type="application/json")

    return render(request, 'apirest/home.html',  {})


