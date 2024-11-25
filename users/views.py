from rest_framework.decorators import action
from rest_framework import mixins , viewsets , status
from rest_framework.response import Response 
from .models import User
from .serializers import UserSerializer , ChangePasswordSerializer



class UserViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
        ):

    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(detail=False , methods=['GET'])
    def profile(self , request):
        user = request.user
        # user = User.objects.get(id = 1)
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)

class AuthViewSet(viewsets.GenericViewSet):
    
    serializer_class = ChangePasswordSerializer
    

    @action(detail=True , methods=['POST'])
    def changepassword(self , request):
        user = request.user
        serializer = ChangePasswordSerializer(user)
        return Response(serializer.data)