from django.test import RequestFactory, TestCase  # type: ignore
from django.urls import reverse  # type: ignore
from django.contrib.auth.models import User, AnonymousUser  # type: ignore
from .models import Value, Characteristic  # type: ignore
from mixer.backend.django import mixer  # type: ignore
import pytest  # type: ignore
from .views import *  # type: ignore


# @pytest.fixture
# def value(request, db)
#    return mixer.blend('agile.Value', value_text = request.param)


class UserViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="keembasilio@gmail.com", password="secret_pw"
        )

    # Testing123 viewing of IndexView with an account which should have response code 200
    def test_index_view_authenticated(self):
        request = self.factory.get("/agile/")
        request.user = self.user
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # Test viewing of ValueView with an account which should have response code 200
    def test_value_view_authenticated(self):
        request = self.factory.get("/agile/value")
        request.user = self.user
        response = ValueView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # Test viewing of CharacteristicView with an account which should have response code 200
    def test_characteristic_view_authenticated(self):
        request = self.factory.get("agile/characteristic")
        request.user = self.user
        response = CharacteristicView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # Test viewing of IndexView without an account which should have response code 302
    def test_index_view_unauthenticated(self):
        request = self.factory.get("/agile/")
        request.user = AnonymousUser()
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    # Test viewing of ValueView without an account which should have response code 302
    def test_value_view_unauthenticated(self):
        request = self.factory.get("/agile/value")
        request.user = AnonymousUser()
        response = ValueView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    # Test viewing of CharacteristicView without an account which should have response code 302
    def test_characteristic_view_unauthenticated(self):
        request = self.factory.get("agile/characteristic")
        request.user = AnonymousUser()
        response = CharacteristicView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    # Test IndexView without data in db
    def test_no_data_index_value(self):
        request = self.factory.get("agile/")
        request.user = self.user
        response = IndexView.as_view()(request)
        self.assertContains(response, "Please input some agile values.")

    def test_no_data_index_characteristic(self):
        request = self.factory.get("agile/")
        request.user = self.user
        response = IndexView.as_view()(request)
        self.assertContains(response, "Please input some agile characteristics.")

    # Test ValueView without data in db
    def test_no_values(self):
        request = self.factory.get("agile/value")
        request.user = self.user
        response = ValueView.as_view()(request)
        self.assertContains(response, "Please input an Agile Value.")

    # Test CharacteristicView without data in db
    def test_no_characteristic(self):
        request = self.factory.get("agile/characteristic")
        request.user = self.user
        response = CharacteristicView.as_view()(request)
        self.assertContains(response, "Please input an Agile Characteristic.")

    # Test characteristics and Value POST method views
    def test_add_value(self):
        request = self.factory.post("/agile/add_value/", {"content": "test"})
        response = add_value(request)
        self.assertEqual(response.status_code, 302)

    def test_update_value(self):
        Value.objects.create(value_text="First Text")
        self.assertEqual(str(Value.objects.all()), "<QuerySet [<Value: First Text>]>")
        request = self.factory.post("/update_value/1/", {"content": "Second Text"})
        response = update_value(request, 1)
        self.assertEqual(str(Value.objects.all()), "<QuerySet [<Value: Second Text>]>")

    def test_delete_value(self):
        Value.objects.create(value_text="First Text")
        self.assertEqual(str(Value.objects.all()), "<QuerySet [<Value: First Text>]>")
        request = self.factory.post("/delete_value/1/")
        response = delete_value(request, 1)
        self.assertEqual(str(Value.objects.all()), "<QuerySet []>")

    def test_add_characteristic(self):
        request = self.factory.post("/agile/add_characteristic/", {"content": "test"})
        response = add_characteristic(request)
        self.assertEqual(response.status_code, 302)

    def test_update_characteristic(self):
        Characteristic.objects.create(characteristic_text="First Text")
        print(Characteristic.objects.all())
        self.assertEqual(
            str(Characteristic.objects.all()),
            "<QuerySet [<Characteristic: First Text>]>",
        )
        request = self.factory.post(
            "/update_characteristic/1/", {"content": "Second Text"}
        )
        response = update_characteristic(request, 1)
        self.assertEqual(
            str(Characteristic.objects.all()),
            "<QuerySet [<Characteristic: Second Text>]>",
        )

    def test_delete_characteristic(self):
        Characteristic.objects.create(characteristic_text="First Text")
        self.assertEqual(
            str(Characteristic.objects.all()),
            "<QuerySet [<Characteristic: First Text>]>",
        )
        request = self.factory.post("/delete_characteristic/1/")
        response = delete_characteristic(request, 1)
        self.assertEqual(str(Characteristic.objects.all()), "<QuerySet []>")
