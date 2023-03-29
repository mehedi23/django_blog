from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)