from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer
from .models import Product

# Create your views here.

@api_view()
def home_view(request,*args,**kwargs):
    """
    This is the home view
    :param request: Request object
    :param args: Input arguments
    :param kwargs: Input keyword arguments

    :return: Response object with the data
    """
    products=Product.objects.all()
    data={}
    if products:
        serializer=ProductSerializer(products,many=True)
        data=serializer.data
    return Response(data)

class HomeAPIView(APIView):
    """
    This is the home API view for GET and POST requests
    """
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        """
        This is the get request for home view
        :param request: Request object
        :param args: Input arguments
        :param kwargs: Input keyword arguments

        :return: Response object with the data
        """
        products=Product.objects.all()
        data={}
        if products:
            serializer=ProductSerializer(products,many=True)
            data=serializer.data
            # raise serializers.ValidationError({'name': 'Please enter a valid name.'})
            
        return Response(data)
    
    def post(self,request,*args,**kwargs):
        """
        This is the post request for home view
        :param request: Request object
        :param args: Input arguments
        :param kwargs: Input keyword arguments

        :return: Response object with the data
        """
        data=request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)