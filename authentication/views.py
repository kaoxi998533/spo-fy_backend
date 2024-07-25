# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from accounts.models import Profile
from django.core.mail import send_mail
import random
import string
from .models import TmpUser

class CustomRegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try: 
            data = request.data
            password = data.get('password')
            email = data.get('email')
            username = data.get('username')
            if not password:
                return Response({'error': 'Password required'}, status=status.HTTP_400_BAD_REQUEST)

            if TmpUser.objects.get(email=email).is_verified != True:
                return Response({'error' : 'The email has not been verified yet' }, status=status.HTTP_400_BAD_REQUEST)


            tmp_user = TmpUser.objects.get(email=email)
            exists = User.objects.filter(email=tmp_user.email).exists()
            if exists:
                return Response({'error' : 'The email has already been registered' }, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(email=tmp_user.email, username=tmp_user.email, is_active=True)
            profile = Profile.objects.get(user=user)
            profile.username = username
            profile.save()
            user.set_password(password)
            user.save()
                
            return Response({'message' : 'Registration successful'})
        except Exception as e:
            return Response({'error' : f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            
        

class CustomSendVerificationCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            email = data.get('email')

            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

            # Handle TmpUser creation and verification code generation
            tmp_user, created = TmpUser.objects.get_or_create(email=email)
            if created or not tmp_user.verification_code:
                verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                tmp_user.verification_code = verification_code
                tmp_user.save()

            send_mail(
                'Email Verification',
                f'Your verification code is: {tmp_user.verification_code}',
                recipient_list=[email],
                from_email=None,
                fail_silently=False
            )

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Verification code sent to email'}, status=status.HTTP_201_CREATED)

class CustomVerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        email = data.get('email')
        code = data.get('code')

        if not email or not code:
            return Response({'error': 'Email and code are required'}, status=status.HTTP_400_BAD_REQUEST)

        tmp_user = TmpUser.objects.get(email=email)
        try:
            if tmp_user.verification_code == code:
                tmp_user.is_verified = True
                tmp_user.save()
                return Response({'message': 'Email verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        except tmp_user.DoesNotExist:
            return Response({'error': 'Have not send verifying email yet'}, status=status.HTTP_400_BAD_REQUEST)
