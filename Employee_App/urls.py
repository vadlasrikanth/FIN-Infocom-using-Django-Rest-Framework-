from django.urls import path,include
from Employee_App.views import EmployeeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee',EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
]