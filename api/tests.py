import requests
from django.test import TestCase
import requests


# Create your tests here.


class GetTest(TestCase):
    def test_unit_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/unit')
        print(response.status_code)
        assert response.status_code == 200

    def test_machine_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/machine')
        assert response.status_code == 200

    def test_user_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/users')
        assert response.status_code == 200

    def test_warranty_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/warranty')
        assert response.status_code == 200

    def test_shipment_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/shipment')
        assert response.status_code == 200

    def test_role_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/roles')
        assert response.status_code == 200

    def test_node_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/node')
        assert response.status_code == 200

    def test_tool_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/tool')
        assert response.status_code == 200

    def test_repairappl_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/repairappl')
        assert response.status_code == 200

    def test_customer_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/customer')
        assert response.status_code == 200

    def test_employee_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/employee')
        assert response.status_code == 200

    def test_order_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/orders')
        assert response.status_code == 200

    def test_ordertype_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/ordertype')
        assert response.status_code == 200

    def test_machine_type_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/machinetype')
        assert response.status_code == 200

    def test_component_type_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/component')
        assert response.status_code == 200

    def test_shop_type_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/shop')
        assert response.status_code == 200

    def test_component_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/machine')
        assert response.status_code == 200

    def test_shop_correct_response(self):
        response = requests.get(url='http://localhost:8080/api/select/shop')
        assert response.status_code == 200
