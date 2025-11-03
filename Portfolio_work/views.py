from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
import requests

# Create your views here.
# def work(request):
#     return render(request, 'portfolio.html')


# @api_view(['GET'])
# def project_list_api(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def portfolio(request):
    projects_qs = Project.objects.all()
    serializer = ProjectSerializer(projects_qs, many=True, context={'request': request})
    projects = serializer.data
    return render(request, 'portfolio.html', {'projects': projects})