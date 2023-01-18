from rest_framework import permissions, viewsets


class PublicViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
