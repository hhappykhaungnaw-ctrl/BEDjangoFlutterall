
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *



class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.select_related("currency").all()
    serializer_class = CountrySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related("parent_dept").all()
    serializer_class = DepartmentSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.select_related("country").all()
    serializer_class = BranchSerializer


class CustodianViewSet(viewsets.ModelViewSet):
    queryset = Custodian.objects.select_related("branch", "dept").all()
    serializer_class = CustodianSerializer
