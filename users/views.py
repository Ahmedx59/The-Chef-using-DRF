from rest_framework.decorators import action
from rest_framework import mixins , viewsets , status
from rest_framework.response import Response 
from .models import User
from .serializers import (
    UserSerializer ,
    ChangePasswordSerializer ,
    SignUPSerializer,
    ActivateSerializer
    )



class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
        ):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return SignUPSerializer
        return super().get_serializer_class()

    @action(detail=False , methods=['GET'])
    def profile(self , request):
        user = request.user
        # user = User.objects.get(id = 1)
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)
    

    @action(detail=True , methods=['post'] , serializer_class = ActivateSerializer )
    def activate(self,request,*args, **kwargs):
        data  = request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Your Account Activated Successfully'})
    
class AuthViewSet(viewsets.GenericViewSet):
    
    serializer_class = ChangePasswordSerializer
    

    @action(detail=True , methods=['POST'])
    def changepassword(self , request):
        user = request.user
        serializer = ChangePasswordSerializer(user)
        return Response(serializer.data)