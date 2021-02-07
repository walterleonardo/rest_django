from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])
def Products(request, *args, **kwargs):
    id = request.GET.get('id',None)
    if request.method == 'GET' and id:
        snippets = Product.objects.filter(pk=id)
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'GET': 
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        if id:
            Product.objects.filter(pk=id).delete()   
            return Response(status=status.HTTP_204_NO_CONTENT)
