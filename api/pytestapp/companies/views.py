from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import Companyserializers
from .models import Company



class CompanyViewSet(ModelViewSet):
    serializer_class = Companyserializers
    queryset = Company.objects.all().order_by('-last_update')
    pagination_class = PageNumberPagination
