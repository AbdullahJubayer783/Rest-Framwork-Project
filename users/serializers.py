from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.UserModel
        fields = '__all__'


##############################################
class RegistrationSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    mobile_no = serializers.IntegerField(required=True)
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','mobile_no','image']
    def save(self):
        username = self.validated_data['username']
        image = self.validated_data['image']
        mobile_no = self.validated_data['mobile_no']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error':"Password dosn't matched!"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already exists!"})
        account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        models.UserModel.objects.create(
            user = account,
            mobile_no = mobile_no,
            image = image,
        )
        return account
##############################################
# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True)
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email','password','confirm_password']
#     def save(self):
#         username = self.validated_data['username']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         confirm_password = self.validated_data['confirm_password']

#         if password != confirm_password:
#             raise serializers.ValidationError({'error':"Password dosn't matched!"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'error':"Email already exists!"})
#         account = User(username=username,email=email,first_name=first_name,last_name=last_name)
#         print(account)
#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account

    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)