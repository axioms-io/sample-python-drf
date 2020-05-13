from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from axioms_drf.authentication import HasValidAccessToken
from axioms_drf.permissions import HasAccessTokenScopes, HasAccessTokenRoles, HasAccessTokenPermissions


class APIPublic(APIView):
    """
    Public API - no authentication required
    """

    def get(self, request, format=None):

        return Response(
            {"message": "Hello from a public endpoint!"}, status=status.HTTP_200_OK
        )


class APIPrivate(APIView):
    authentication_classes = [HasValidAccessToken]
    permission_classes = (HasAccessTokenScopes,)
    access_token_scopes = ["openid", "profile"]  # noqa
    """
    Private API - authentication required
    """

    def get(self, request, format=None):
        return Response(
            {"message": "All good. You are authenticated!"}, status=status.HTTP_200_OK
        )


class SampleRole(APIView):
    """
    Sample role - create, update, read, delete
    """

    authentication_classes = [HasValidAccessToken]
    permission_classes = (HasAccessTokenRoles,)
    access_token_roles = ["sample:role"]  # noqa

    def get(self, request, format=None):
        return Response({"message": "Sample read."}, status=status.HTTP_200_OK,)

    def post(self, request, format=None):
        return Response({"message": "Sample created."}, status=status.HTTP_200_OK,)

    def patch(self, request, format=None):
        return Response({"message": "Sample updated."}, status=status.HTTP_200_OK,)

    def delete(self, request, format=None):
        return Response({"message": "Sample deleted."}, status=status.HTTP_200_OK,)


class SamplePermission(APIView):
    """
    Sample permission applied to method level
    """
    authentication_classes = [HasValidAccessToken]
    permission_classes = (HasAccessTokenPermissions,)

    @property
    def access_token_permissions(self):
        method_permissions = {
            'GET': ["sample:read"] ,
            'POST': ["sample:create"],
            'PATCH': ["sample:update"],
            'DELETE': ["sample:delete"]
        }
        return method_permissions[self.request.method]


    def get(self, request, format=None):
        return Response({"message": "Sample read."}, status=status.HTTP_200_OK,)

    def post(self, request, format=None):
        return Response({"message": "Sample created."}, status=status.HTTP_200_OK,)

    def patch(self, request, format=None):
        return Response({"message": "Sample updated."}, status=status.HTTP_200_OK,)

    def delete(self, request, format=None):
        return Response({"message": "Sample deleted."}, status=status.HTTP_200_OK,)
