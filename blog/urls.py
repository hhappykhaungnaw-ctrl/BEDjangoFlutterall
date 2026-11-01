from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .models import *
from .serializers import *

router =DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'custodians', CustodianViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
