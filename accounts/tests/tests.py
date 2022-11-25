from accounts.models import Account
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from products.models import Product
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status


class AccountAttributtesTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "talita_seller",
            "password": 1234,
            "first_name": "tatita",
            "last_name": "rebouças",
            "is_seller": True,
        }

        cls.account = Account.objects.create(**cls.account_data)

    def test_primary_key(self):

        correct_response = True
        test_response = Account._meta.get_field("id").primary_key
        message = f"Verifique se o campo `primary_key` é um campo `id` {correct_response}"

        self.assertEqual(correct_response, test_response, message)

    def test_username_max_length(self):

        response_max_length = 20
        test_max_length = Account._meta.get_field("username").max_length
        message = f"Verifique se o campo `max_length` de name foi limitado com {response_max_length} characteres"

        self.assertEqual(response_max_length, test_max_length, message)



    def test_first_name_max_length(self):

        expected_max_length = 50
        result_max_length = Account._meta.get_field("first_name").max_length
        message = f"Verifique se o campo `max_length` de name foi definido como {expected_max_length} characteres"

        self.assertEqual(expected_max_length, result_max_length, message)

    def test_last_name_max_length(self):

        name_max_length = 50
        test_max_length = Account._meta.get_field("last_name").max_length
        message = f"Verifique se o campo `max_length` de name foi definido como {name_max_length} characteres"

        self.assertEqual(name_max_length, test_max_length, message)

    def test_duplicated_username_if_not_created(self):
        account_data = {
            "username": self.account.username,
            "password": 1234,
            "first_name": "tatiana",
            "last_name": "oliveira",
            "is_seller": True,
        }

        account = Account(**account_data)
        expected_error_message = "User with this Username already exists."
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            account.full_clean()

    def test_is_seller_default_is_false(self):

        seller_default = False
        test_default = Account._meta.get_field("is_seller").default
        message = f"Verifique se o campo `default` de is_seller foi definido como {seller_default}"

        self.assertEqual(seller_default, test_default, message)


class ProductRelationshipTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "coral",
            "password": "1234",
            "first_name": "coral",
            "last_name": "seller",
            "is_seller": True,
        }

        cls.product_data = {
            "description": "Sorvete de Chocolate Jamaicano",
            "price": 404.88,
            "quantity": 15,
        }

        cls.account = Account.objects.create_user(**cls.account_data)
        cls.product = Product.objects.create(**cls.product_data, seller=cls.account)

    def test_many_to_one_product_and_account(self):

        seller_username = "coral"
        test_seller_username = self.product.seller.username
        msg = f"Verifique se o produto criado pertence ao usuário {seller_username}"

        self.assertEqual(seller_username, test_seller_username, msg)

class AccountSellerTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/accounts/"
        cls.account_data = {
            "username": "Luiz",
            "password": "1234",
            "first_name": "Luiz",
            "last_name": "Marinho",
            "is_seller": True,
        }

        cls.account = Account.objects.create_user(**cls.account_data)

    def test_account_seller_is_created(self):

        expected_value = True
        result_value = self.account.is_seller
        message = "A conta não foi criada, verifique os campos"

        self.assertEqual(expected_value, result_value, message)

class AccountCommonTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/accounts/"
        cls.account_data = {
            "username": "Jairo",
            "password": "1234",
            "first_name": "Jairo",
            "last_name": "Mendes",
            "is_seller": False,
        }

        cls.account = Account.objects.create_user(**cls.account_data)

    def test_account_is_seller_false_is_created(self):

        expected_value = False
        result_value = self.account.is_seller
        message = "Conta não pode ser criada, verifique os campos"

        self.assertEqual(expected_value, result_value, message)
    

class AccountSellerErrorAttributesTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/accounts/"
        cls.account_data = {
            "username": "zambia",
            "password": "1234",
            "wrong_attribute": "Zambia",
            "last_name": "Caraccelli",
            "is_seller": True,
        }

    def test_account_with_invalid_attributes_is_created(self):

        response = self.client.post(self.register_url, self.account_data)

        status_code = status.HTTP_400_BAD_REQUEST
        test_status_code = response.status_code
        message = "A conta não pode ser criada"

        self.assertEqual(status_code, test_status_code, message)



class AccountSellerLoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.login_url = reverse("loggedin")
        user_data = {
            "username": "junior",
            "password": "1234",
            "first_name": "junior",
            "last_name": "ananas",
            "is_seller": True,
        }

        cls.user_login = {
            "username": "junior",
            "password": "1234",
        }

        user = Account.objects.create_user(**user_data)

    def test_seller_login(self):

        login = self.client.post(self.login_url, data=self.user_login)

        self.assertIn("token", login.data)

class AccountsAndPermissionTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user_data_normal = {
            "username": "clara_normal",
            "password": "1234",
            "first_name": "clara",
            "last_name": "normal",
            "is_seller": False,
        }

        user_data_seller = {
            "username": "luna_seller",
            "password": "1234",
            "first_name": "luna",
            "last_name": "seller",
            "is_seller": True,
        }

        user_data_adm = {
            "username": "edna_adm",
            "password": "1234",
            "first_name": "edna",
            "last_name": "adm",
            "is_seller": False,
        }

        cls.admin_user = Account.objects.create_superuser(**user_data_adm)
        cls.seller_user = Account.objects.create_user(**user_data_seller)
        cls.normal_user = Account.objects.create_user(**user_data_normal)

    def test_only_owner_update(self):

        token = Token.objects.create(user=self.normal_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response_owner = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/", {"first_name": "User-is-a-Patched"}
        )
        self.assertIn("User-is-a-Patched", response_owner.data["first_name"])

        ressponse_not_owner = self.client.patch(
            f"/api/accounts/{str(self.seller_user.id)}/", {"first_name": "User-is-a-Patched"}
        )
        self.assertEqual(403, ressponse_not_owner.status_code)

        response_admin = self.client.patch(
            f"/api/accounts/{str(self.admin_user.id)}/", {"first_name": "User-is-a-Patched"}
        )
        self.assertEqual(403, response_admin.status_code)

    def test_only_admin_deactivate_user(self):

        token = Token.objects.create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_admin = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": False}
        )
        self.assertEqual(200, response_admin.status_code)

        token = Token.objects.create(user=self.normal_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_normal = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": False}
        )
        self.assertEqual(401, response_normal.status_code)

        token = Token.objects.create(user=self.seller_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_seller = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": False}
        )
        self.assertEqual(403, response_seller.status_code)

    def test_only_admin_reactivate_user(self):

        token = Token.objects.create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_admin = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": True}
        )
        self.assertEqual(200, response_admin.status_code)

        token = Token.objects.create(user=self.normal_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_normal = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": True}
        )
        self.assertEqual(403, response_normal.status_code)

        token = Token.objects.create(user=self.seller_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response_seller = self.client.patch(
            f"/api/accounts/{str(self.normal_user.id)}/management/", {"is_active": True}
        )
        self.assertEqual(403, response_seller.status_code)


