from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
import io
from .serializers import BlogContentSerializer
from .models import BlogContent
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.


def home(request):
    return HttpResponse("this is a home page")

@api_view(['GET'])
def ShowAll(request):
    blogset = BlogContent.objects.all()
    serializer = BlogContentSerializer(blogset,many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def Create(request):
    if request.method == 'POST': 
        try:
            stream = io.BytesIO(request.body)
            parsed_data = JSONParser().parse(stream)
            deserialize = BlogContentSerializer(data=parsed_data) 
            if deserialize.is_valid():
                deserialize.save()
                return Response("Successfully saved")
            else:
                return Response(deserialize.errors)
        except:
            return Response("Invalid data")        

    blogset = BlogContent.objects.all()
    serializer = BlogContentSerializer(blogset,many = True)
    return Response(serializer.data)   


@api_view(['PUT'])
def Create_ID(request,pk):
    if request.method == 'PUT': 
        try:
            stream = io.BytesIO(request.body)
            parsed_data = JSONParser().parse(stream)
            try:
                blogobj = BlogContent.objects.get(id=pk)
            except:
                return Response("Invalid id")
            deserialize = BlogContentSerializer(blogobj,data=parsed_data,partial = True) 
            if deserialize.is_valid():
                deserialize.save()
                return Response("Successfully saved")
            else:
                return Response(deserialize.errors)
        except:
            return Response("Invalid data")        

   

        





