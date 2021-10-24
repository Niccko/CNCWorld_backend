from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls import url
from rest_framework import permissions

from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="CNC API",
        default_version='v1',
        description="CNC objects description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), ),
    path('tables/', get_table_list_view),
    path('select/<str:table_name>', SelectView.as_view()),
    path('insert/<str:table_name>', InsertView.as_view()),
    path('delete/<str:table_name>', DeleteView.as_view()),
    path('update/<str:table_name>', UpdateView.as_view()),

    # path('unit/', UnitListView.as_view()),
    # path('machinetype/', MachineTypeListView.as_view()),
    # path('component/', ComponentListView.as_view()),
    # path('componenttype/', ComponentTypeListView.as_view()),
    # path('tool/', ToolListView.as_view()),
    # path('machine/', MachineListView.as_view()),
    # path('role/', RoleListView.as_view()),
    # path('node/', NodeListView.as_view()),
    # path('shoptype/', ShopTypeListView.as_view()),
    # path('shop/', ShopListView.as_view()),
    # path('employee/', EmployeeListView.as_view()),
    # path('customer/', CustomerListView.as_view()),
    # path('warranty/', WarrantyListView.as_view()),
    # path('ordertype/', OrderTypeListView.as_view()),
    # path('order/', OrderListView.as_view()),
    # path('shipment/', ShipmentListView.as_view()),
    # path('user/', UserListView.as_view()),
    # path('repairappl/', RepairApplListView.as_view()),
    #
    # path('unit/<int:pk>/', UnitDetailView.as_view()),
    # path('machinetype/<int:pk>/', MachineTypeDetailView.as_view()),
    # path('component/<int:pk>/', ComponentDetailView.as_view()),
    # path('componenttype/<int:pk>/', ComponentTypeDetailView.as_view()),
    # path('tool/<int:pk>/', ToolDetailView.as_view()),
    # path('machine/<str:pk>/', MachineDetailView.as_view()),
    # path('role/<int:pk>/', RoleDetailView.as_view()),
    # path('node/<int:pk>/', NodeDetailView.as_view()),
    # path('shoptype/<int:pk>/', ShopTypeDetailView.as_view()),
    # path('shop/<int:pk>/', ShopDetailView.as_view()),
    # path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    # path('customer/<int:pk>/', CustomerDetailView.as_view()),
    # path('warranty/<int:pk>/', WarrantyDetailView.as_view()),
    # path('ordertype/<int:pk>/', OrderTypeDetailView.as_view()),
    # path('order/<int:pk>/', OrderDetailView.as_view()),
    # path('shipment/<int:pk>/', ShipmentDetailView.as_view()),
    # path('user/<int:pk>/', UserDetailView.as_view()),
    # path('repairappl/<int:pk>/', RepairApplDetailView.as_view()),

    path('insert/', InsertView.as_view())
]
