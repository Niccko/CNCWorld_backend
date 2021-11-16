from django.db.models import *


class MachineType(Model):
    id = AutoField(primary_key=True)
    typename = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "machinetype"


class ComponentType(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "componenttype"


class Component(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    quantity = IntegerField()
    price = IntegerField()
    provider = IntegerField()
    component_type = ForeignKey(ComponentType, on_delete=CASCADE, db_column='id_componenttype')

    class Extra:
        service = False

    class Meta:
        db_table = "component"


class Tool(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "tool"


class Machine(Model):
    id = CharField(primary_key=True, max_length=255)
    price = IntegerField()
    blueprint = CharField(max_length=255)
    description = CharField(max_length=255)
    id_machinetype = ForeignKey(MachineType, on_delete=CASCADE, db_column='id_machinetype')
    tools = ManyToManyField(Tool, through='RequiredTools', through_fields=['id_machine', 'id_tool'])

    class Extra:
        service = False

    class Meta:
        db_table = "machine"


class Unit(Model):
    id = AutoField(primary_key=True)
    allowed = BooleanField()
    status = CharField(max_length=255)
    date_manufactured = DateField(db_column='datemanufactured')
    id_machine = ForeignKey(Machine, on_delete=CASCADE, db_column='id_machine')

    class Extra:
        service = False

    class Meta:
        db_table = "unit"


class Node(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    blueprint = CharField(max_length=255)
    id_machine = ForeignKey(Machine, on_delete=CASCADE, db_column='id_machine')

    class Extra:
        service = False

    class Meta:
        db_table = "node"


class Composition(Model):
    id_component = ForeignKey(Component, on_delete=CASCADE)
    id_node = ForeignKey(Node, on_delete=CASCADE, db_column='id_node')

    class Extra:
        service = True

    class Meta:
        db_table = "composition"


class RequiredTools(Model):
    id_machine = ForeignKey(Machine, on_delete=CASCADE, db_column='id_machine')
    id_tool = ForeignKey(Tool, on_delete=CASCADE, db_column='id_tool')

    class Extra:
        service = True

    class Meta:
        db_table = "requiredtools"


class ShopType(Model):
    id = AutoField(primary_key=True)
    type = CharField(max_length=255, db_column='type')

    class Extra:
        service = False

    class Meta:
        db_table = "shoptype"


class Shop(Model):
    id = AutoField(primary_key=True)
    address = CharField(max_length=255)
    phone = CharField(max_length=255)
    id_ShopType = ForeignKey(ShopType, on_delete=CASCADE, db_column='id_shoptype')

    class Extra:
        service = False

    class Meta:
        db_table = "shop"


class Employee(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    salary = IntegerField()
    id_Shop = ForeignKey(Shop, on_delete=CASCADE, db_column='id_shop')

    class Extra:
        service = False

    class Meta:
        db_table = "employee"


class Customer(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    phone = CharField(max_length=255)
    email = CharField(max_length=255)
    address = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "customer"


class Warranty(Model):
    id = AutoField(primary_key=True)
    expiredate = DateField()

    class Extra:
        service = False

    class Meta:
        db_table = "warranty"


class OrderType(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "ordertype"


class Orders(Model):
    id = AutoField(primary_key=True)
    date = DateField()
    status = CharField(max_length=255)
    id_Employee = ForeignKey(Employee, on_delete=CASCADE, db_column='id_employee')
    id_Warranty = ForeignKey(Warranty, on_delete=CASCADE, db_column='id_warranty')
    id_Customer = ForeignKey(Customer, on_delete=CASCADE, db_column='id_customer')
    id_OrderType = ForeignKey(OrderType, on_delete=CASCADE, db_column='id_ordertype')

    class Extra:
        service = False

    class Meta:
        db_table = "orders"


class Shipment(Model):
    id = AutoField(primary_key=True)
    price = IntegerField()
    comment = CharField(max_length=255)
    id_Customer = ForeignKey(Customer, on_delete=CASCADE, db_column='id_customer')

    class Extra:
        service = False

    class Meta:
        db_table = "shipment"


class Roles(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)

    class Extra:
        service = False

    class Meta:
        db_table = "roles"


class Users(Model):
    id = AutoField(primary_key=True)
    password = CharField(max_length=255)
    id_customer = ForeignKey(Customer, on_delete=CASCADE, db_column='id_customer')
    roles = ManyToManyField(Roles, through='UserRoles', through_fields=['id_user', 'id_roles'])

    class Extra:
        service = False

    class Meta:
        db_table = "users"


class UserRoles(Model):
    id = AutoField(primary_key=True)
    id_user = ForeignKey(Users, on_delete=CASCADE, db_column='id_user')
    id_roles = ForeignKey(Roles, on_delete=CASCADE, db_column='id_roles')
    class Extra:
        service = True

    class Meta:
        db_table = "userroles"


class RepairAppl(Model):
    id = AutoField(primary_key=True)
    comment = CharField(max_length=255)
    date = DateField()
    status = CharField(max_length=255)
    period = DateField()
    id_Customer = ForeignKey(Customer, on_delete=CASCADE, db_column='id_customer')
    id_Machine = ForeignKey(Machine, on_delete=CASCADE, db_column='id_machine')

    class Extra:
        service = False

    class Meta:
        db_table = "repairappl"
