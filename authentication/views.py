# authentication/views.py

from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.models import EmailConfirmationHMAC
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response

class CustomVerifyEmailView(VerifyEmailView):
    def get(self, request, *args, **kwargs):
        key = kwargs.get('key')
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        
        if email_confirmation:
            email_confirmation.confirm(request)
            user = email_confirmation.email_address.user
            
            # Specify the authentication backend
            backend = 'allauth.account.auth_backends.AuthenticationBackend'
            user.backend = backend
            
            if user.is_active:
                login(request, user, backend=backend)
                return redirect('f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"')  # Redirect to a success URL after login
        
        return Response({'detail': 'Invalid key'}, status=status.HTTP_400_BAD_REQUEST)

