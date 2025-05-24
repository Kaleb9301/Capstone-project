from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, serializer.data)
