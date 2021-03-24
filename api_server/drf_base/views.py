from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def test(request):
    return HttpResponse('hello pablo!')

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def test_jason(request):
    return Response({"name":"Jason Mayne"})
