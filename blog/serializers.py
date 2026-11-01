
from rest_framework import serializers
from .models import Currency, Country, Department, Branch, Custodian


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class CustodianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custodian
        fields = "__all__"
