from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, CustomTokenObtainPairSerializer

class RegisterUserView(APIView):
    http_method_names = ['post']
    serializer_class = UserSerializer
    
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            # get_user_model().objects.create_user(**serializer.validated_data)
            serializer.save()
            return Response(data={
                'message': 'User created successfully',
                'data': serializer.data}, status=201
            )
        
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer