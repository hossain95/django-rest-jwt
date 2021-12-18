from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Posts
from .serializers import PostSerializer

# Create your views here.


class PostView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)