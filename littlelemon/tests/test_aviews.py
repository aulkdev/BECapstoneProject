from django.test import TestCase, Client
from restaurant.models import Booking,Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
client = Client()
class ViewTestCase(TestCase):
    def setup(self):
        Menu.objects.create(id=2,title="IceCream", price=80, inventory=100)
        Menu.objects.create(id=1,title="IceCream2", price=20, inventory=100)
    def test_getall(self):
        self.setup()
        response = client.get(reverse('MenuItemView'))
        items = Menu.objects.all()
        sitems = MenuSerializer(items, many=True)
        self.assertEqual(response.data, sitems.data)
