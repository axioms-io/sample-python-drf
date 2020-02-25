from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from axioms_drf.authentication import  AccessTokenAuthentication
from axioms_drf.permissions import AccessScopePermission

class Public(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello from a public endpoint!'}, status=status.HTTP_200_OK)

class Private(APIView):
    authentication_classes = [AccessTokenAuthentication]
    permission_classes = (AccessScopePermission,)
    access_token_scopes = ['openid', 'profile']  # noqa
    def get(self, request, format=None):
        return Response({'message': 'All good. You are authenticated!'}, status=status.HTTP_200_OK)

class Admin(APIView):
    authentication_classes = [AccessTokenAuthentication]
    permission_classes = (AccessScopePermission,)
    access_token_scopes = ['tenant:owner', 'user:admin']  # noqa

    def get(self, request, format=None):
        return Response({'message': 'All good. You are authenticated as admin!'}, status=status.HTTP_200_OK)