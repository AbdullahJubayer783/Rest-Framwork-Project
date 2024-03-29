from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login , logout
from . import models
from django.contrib.auth.tokens import default_token_generator
from . import serializers
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
# Create your views here.

class BuiltInUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.BuiltInUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id',]

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            
            token = default_token_generator.make_token(user)
            print("token",token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid",uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html',{'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Check Your Mail For Confirmation..")
        return Response(serializer.errors)

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register") 
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                # Check if the user is staff
                if user.is_staff:
                    login(request, user)
                    return Response({'token': token.key, 'user_id': user.id,'staff':True})
                else:
                    login(request, user)
                    return Response({'token': token.key, 'user_id': user.id,'staff':False})
            else:
                return Response({'error': "Invalid Credentials"})
        return Response(serializer.errors)
    
class UserLogoutApiView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)