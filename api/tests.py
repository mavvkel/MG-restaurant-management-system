from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIRequestFactory, APITestCase
from decimal import Decimal
from RMS.models.DishRestaurantMenuEntry import *
from RMS.models.DrinkRestaurantMenuEntry import *
from RMS.models.RestaurantMenuEntry import *
from RMS.models.RestaurantTable import *
from api.views import RestaurantMenuEntryListView, RestaurantMenuEntryDetailView


class RestaurantMenuEntryListViewTests(APITestCase):
    def setUp(self) -> None:
        RestaurantMenuEntry.objects.all().delete()
        self.assertEqual(DishRestaurantMenuEntry.objects.all().exists(), False)
        self.eggs = DishRestaurantMenuEntry.objects.create(name='Eggs Benedict',
                                                           price=Decimal('29.99'),
                                                           stage=DishRestaurantMenuEntry.DishStage.MAIN_COURSE,
                                                           weight=Decimal('0.3'))
        self.toast = DishRestaurantMenuEntry.objects.create(name='Toast with ham',
                                                            price=Decimal('9.99'),
                                                            stage=DishRestaurantMenuEntry.DishStage.STARTER,
                                                            weight=Decimal('0.1'))
        self.coke = DrinkRestaurantMenuEntry.objects.create(name='Coca Cola',
                                                            price=Decimal('2.99'),
                                                            volume=Decimal('0.33'))
        self.booze = DrinkRestaurantMenuEntry.objects.create(name='Heineken',
                                                             price=Decimal('5.40'),
                                                             contains_alcohol=True,
                                                             volume=Decimal('0.5'))

        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(len(User.objects.all()), 1)

    def test_get_RestaurantMenuEntry_list(self):
        """
        Ensure unauthenticated GET method on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:menu_entry_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 4)
        self.assertContains(response=response,
                            text='Eggs Benedict',
                            count=1,
                            status_code=200)
        self.assertContains(response=response,
                            text='Toast with ham',
                            count=1,
                            status_code=200)
        self.assertContains(response=response,
                            text='Coca Cola',
                            count=1,
                            status_code=200)
        self.assertContains(response=response,
                            text='Heineken',
                            count=1,
                            status_code=200)

    def test_post_Dish_to_RestaurantMenuEntry_list(self):
        """
        Ensure unauthenticated POST method with DishRestaurantMenuEntry on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:menu_entry_list')
        data = \
            {
                'name': 'Scrambled eggs',
                'price': '20.54',
                'stage': '2',
                'weight': '0.250',
                'resourcetype': 'DishRestaurantMenuEntry'
            }

        previous_count = DishRestaurantMenuEntry.objects.count()
        response = self.client.post(url, data, format='json')
        # force_authenticate(request, user=self.test_user1)
        self.assertContains(response=response,
                            text='Scrambled eggs',
                            count=1,
                            status_code=201)
        self.assertEqual(DishRestaurantMenuEntry.objects.count(), previous_count + 1)
        self.assertTrue(DishRestaurantMenuEntry.objects.filter(name='Scrambled eggs').exists())

    def test_post_Drink_to_RestaurantMenuEntry_list(self):
        """
        Ensure unauthenticated POST method with DrinkRestaurantMenuEntry on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:menu_entry_list')
        data = \
            {
                'name': 'Fanta',
                'price': '1.39',
                'contains_alcohol': False,
                'volume': '0.33',
                'resourcetype': 'DrinkRestaurantMenuEntry'
            }

        previous_count = DrinkRestaurantMenuEntry.objects.count()
        response = self.client.post(url, data, format='json')
        # force_authenticate(request, user=self.test_user1)
        self.assertContains(response=response,
                            text='Fanta',
                            count=1,
                            status_code=201)
        self.assertEqual(DrinkRestaurantMenuEntry.objects.count(), previous_count + 1)
        self.assertTrue(DrinkRestaurantMenuEntry.objects.filter(name='Fanta').exists())


class RestaurantTableListViewTests(APITestCase):
    def setUp(self) -> None:
        RestaurantMenuEntry.objects.all().delete()
        self.assertEqual(DishRestaurantMenuEntry.objects.all().exists(), False)
        self.smallTable = RestaurantTable.objects.create(capacity=int(4),
                                                         properties=RestaurantTable.RestaurantTableProperty.NEAR_WINDOW)
        self.bigTable = RestaurantTable.objects.create(capacity=int(12),
                                                       properties=RestaurantTable.RestaurantTableProperty.IN_BAR)

        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(len(User.objects.all()), 1)

    def test_get_RestaurantTable_list(self):
        """
        Ensure unauthenticated GET method on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:restaurant_table_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
        self.assertContains(response=response,
                            text='"capacity":4,"properties":1',
                            count=1,
                            status_code=200)
        self.assertContains(response=response,
                            text='"capacity":12,"properties":4',
                            count=1,
                            status_code=200)

    def test_post_Table_to_RestaurantTable_list(self):
        """
        Ensure unauthenticated POST method with DishRestaurantMenuEntry on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:restaurant_table_list')
        data = \
            {
                'capacity': '2',
                'properties': f'{RestaurantTable.RestaurantTableProperty.IN_BAR}'
            }

        previous_count = RestaurantTable.objects.count()
        response = self.client.post(url, data, format='json')
        # force_authenticate(request, user=self.test_user1)
        self.assertContains(response=response,
                            text='"capacity":2,"properties":4',
                            count=1,
                            status_code=201)
        self.assertEqual(RestaurantTable.objects.count(), previous_count + 1)
        self.assertTrue(RestaurantTable.objects.filter(capacity=2, properties=RestaurantTable.RestaurantTableProperty.
                                                       IN_BAR).exists())

        response = self.client.get(url, format='json')
        self.assertContains(response=response,
                            text='"properties":4',
                            count=2,
                            status_code=200)
