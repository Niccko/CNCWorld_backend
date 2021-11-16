from abc import ABC

from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method
from rest_framework.serializers import *
from .models import *
from rest_framework import serializers


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class MachineTypeSerializer(ModelSerializer):
    class Meta:
        model = MachineType
        fields = "__all__"


class ComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = "__all__"


class ComponentTypeSerializer(ModelSerializer):
    class Meta:
        model = ComponentType
        fields = "__all__"


class ToolSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class MachineSerializer(ModelSerializer):
    tools = ToolSerializer(many=True)

    class Meta:
        model = Machine
        fields = '__all__'


class NodeSerializer(ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields = "__all__"


class RequiredToolsSerializer(ModelSerializer):
    class Meta:
        model = RequiredTools
        fields = "__all__"


class ShopTypeSerializer(ModelSerializer):
    class Meta:
        model = ShopType
        fields = "__all__"


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class WarrantySerializer(ModelSerializer):
    class Meta:
        model = Warranty
        fields = "__all__"


class OrderTypeSerializer(ModelSerializer):
    class Meta:
        model = OrderType
        fields = "__all__"


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class UserRolesSerializer(ModelSerializer):
    class Meta:
        model = UserRoles
        fields = "__all__"


class RepairApplSerializer(ModelSerializer):
    class Meta:
        model = RepairAppl
        fields = "__all__"


name_to_serializer = {
    "machinetype": MachineTypeSerializer,
    "componenttype": ComponentTypeSerializer,
    "component": ComponentSerializer,
    "tool": ToolSerializer,
    "machine": MachineSerializer,
    "unit": UnitSerializer,
    "node": NodeSerializer,
    "composition": CompositionSerializer,
    "shoptype": ShopTypeSerializer,
    "shop": ShopSerializer,
    "employee": EmployeeSerializer,
    "customer": CustomerSerializer,
    "warranty": WarrantySerializer,
    "ordertype": OrderTypeSerializer,
    "orders": OrdersSerializer,
    "shipment": ShipmentSerializer,
    "roles": RolesSerializer,
    "users": UsersSerializer,
    "userroles": UserRolesSerializer,
    "repairappl": RepairApplSerializer
}
