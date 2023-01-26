from django.test import TestCase
from restaurant.models import Menu


class TestMenu(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(id=787, title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")