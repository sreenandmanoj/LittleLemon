from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title='Banana dessert',
            price=5.6,
            inventory=20
        )
        self.assertEqual(item.title,"Banana dessert")
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(
            title='Banana dessert',
            price=5.6,
            inventory=20
        )
        
        Menu.objects.create(
            title='Vainilla Icecream',
            price=2.50,
            inventory=12
        )


        Menu.objects.create(
            title='Banana split',
            price=10.5,
            inventory=40
        )
    
    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus,many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),serializer.data)
        
    

