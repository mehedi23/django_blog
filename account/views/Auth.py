from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import RegistraionSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }


class RegistrationView(APIView):
    def post(self, request, format=None):
        serializer = RegistraionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)

            return Response({
                'token' : token,
                'msg' : 'Registration Success'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = authenticate(email= email, password = password)

            if user is not None:
                token = get_tokens_for_user(user)

                return Response({
                    'token' : token,
                    'msg' : 'Log In Success'
                }, status=status.HTTP_200_OK)
            else :
                return Response({
                    'error' : {
                        'msg' : [ 'Email or password is not valid' ]
                    }
                }, status=status.HTTP_404_NOT_FOUND)
            


class TokenRefreshView(APIView):
    def post(self, request, format=None):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({
                'error' : {
                    'msg' : ['Refresh token is required']
                }
            },status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
        except:
            return Response({
                'error' : {
                    'msg' : ['Invalid refresh token']
                }
            },status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'access' : access_token
        },status=status.HTTP_201_CREATED)