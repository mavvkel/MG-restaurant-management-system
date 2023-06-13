from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIRequestFactory, APITestCase
from decimal import Decimal
from rest_framework import status
from RMS.models.DishRestaurantMenuEntry import *
from RMS.models.DrinkRestaurantMenuEntry import *
from RMS.models.RestaurantMenuEntry import *
from RMS.models.RestaurantTable import *
from RMS.models.RestaurantTableBooking import RestaurantTableBooking
from RMS.models.StartEndHours import StartEndHours
from api.serializers import RestaurantTableBookingSerializer
from api.views import RestaurantMenuEntryListView, RestaurantMenuEntryDetailView

from datetime import date, datetime


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
        RestaurantTable.objects.all().delete()
        self.assertEqual(RestaurantTable.objects.all().exists(), False)
        self.smallTable = RestaurantTable.objects.create(capacity=4)
        self.smallTable.properties.add(RestaurantTableProperty.objects.create(property=1))

        self.bigTable = RestaurantTable.objects.create(capacity=12)
        self.bigTable.add_property(RestaurantTableProperty.objects.create(property=4))
        self.smallTable.add_property(RestaurantTableProperty.objects.create(property=4))
        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(User.objects.count(), 1)

    def test_get_RestaurantTable_list(self):
        """
        Ensure unauthenticated GET method on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:restaurant_table_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
        self.assertContains(response=response,
                            text='"capacity":4,"properties":[{"property":1},{"property":4}]',
                            count=1,
                            status_code=200)
        self.assertContains(response=response,
                            text='"capacity":12,"properties":[{"property":4}]',
                            count=1,
                            status_code=200)

    def test_post_Table_to_RestaurantTable_list(self):
        """
        Ensure unauthenticated POST method with DishRestaurantMenuEntry on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:restaurant_table_list')
        data = {
            'capacity': 2,  # Update this line
            'properties': [{'property': 4}]
        }

        previous_count = RestaurantTable.objects.count()
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RestaurantTable.objects.count(), previous_count + 1)
        self.assertTrue(RestaurantTable.objects.filter(capacity=2, properties__property=4).exists())

        response = self.client.get(url, format='json')
        self.assertContains(response=response,
                            text='"properties":[{"property":4}]',
                            count=2,
                            status_code=200)


class StartEndHoursViewTests(APITestCase):
    def setUp(self) -> None:
        StartEndHours.objects.all().delete()
        self.startEndHoursTemp = StartEndHours.objects.create(start_time=datetime.fromisoformat(
                                                                '2011-11-04T00:05:23+04:00').time(),
                                                              end_time=datetime.fromisoformat(
                                                                  '2011-11-04T00:06:23+04:00').time())

        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(StartEndHours.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)

    def test_get_StartEndHours(self):
        url = reverse('api:start_end_hours')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertContains(response=response,
                            text='"start_time":"00:05:23","end_time":"00:06:23"',
                            count=1,
                            status_code=200)

    def test_post_StartEndHours(self):
        url = reverse('api:start_end_hours')
        data = {
            'start_time': '10:02:23',
            'end_time': '19:02:23'
        }

        previous_count = StartEndHours.objects.count()
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StartEndHours.objects.count(), previous_count + 1)
        self.assertTrue(StartEndHours.objects.filter(start_time=datetime.fromisoformat(
                                                                '2011-11-04T10:02:23+04:00').time()
                                                     , end_time=datetime.fromisoformat(
                                                                '2011-11-04T19:02:23+04:00').time()).exists())

        response = self.client.get(url, format='json')
        self.assertContains(response=response,
                            text='"start_time":"10:02:23","end_time":"19:02:23"',
                            count=1,
                            status_code=200)


class RestaurantTableBookingViewTests(APITestCase):
    def setUp(self) -> None:
        RestaurantTable.objects.all().delete()
        RestaurantTableBooking.objects.all().delete()

        self.smallTable = RestaurantTable.objects.create(capacity=4)
        self.smallTable.properties.add(RestaurantTableProperty.objects.create(property=4))

        start_time_temp = datetime.fromisoformat('2011-11-04T00:05:23+04:00').time()
        end_time_temp = datetime.fromisoformat('2011-11-04T00:06:23+04:00').time()
        self.startEndHoursTemp = StartEndHours.objects.create(start_time=start_time_temp, end_time=end_time_temp)

        self.assertEqual(RestaurantTableBooking.objects.all().exists(), False)
        self.booking_test = RestaurantTableBooking.objects.create(table=self.smallTable,
                                                                  date=datetime.now(),
                                                                  startEndHours=self.startEndHoursTemp)

        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(User.objects.count(), 1)

    def test_get_RestaurantTable_booking(self):
        """

        """
        url = reverse('api:restaurant_table_booking')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertContains(response=response,
                            text='"table":{"id":1,"capacity":4,"properties":[{"property":4}]},"startEndHours":'
                                 '{"start_time":"00:05:23","end_time":"00:06:23"},"date":"2023-06-13"}]',
                            count=1,
                            status_code=200)

    def test_post_RestaurantTableBooking(self):
        """
        Ensure unauthenticated POST method with DishRestaurantMenuEntry on /api/restaurant/menu endpoint is working.
        """
        url = reverse('api:restaurant_table_booking')
        data = {
            'startEndHours': {"start_time": "20:05:23", "end_time": "21:06:23"},
            'table': {'capacity': 2, "properties": [{"property": 5}, {"property": 1}]},
            'date': "2023-06-13"
        }

        previous_count = RestaurantTableBooking.objects.count()
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RestaurantTableBooking.objects.count(), previous_count + 1)

        response = self.client.get(url, format='json')
        self.assertContains(response=response,
                            text='"table":{"id":2,"capacity":2,"properties":[{"property":5},{"property":1}]},"startEndHours":'
                                 '{"start_time":"20:05:23","end_time":"21:06:23"},"date":"2023-06-13"}]',
                            count=1,
                            status_code=200)
        # {"id":2,"table":{"id":2,"capacity":2,"properties":[{"property":5},{"property":1}]},
        # "startEndHours":{"start_time":"20:05:23","end_time":"21:06:23"},"date":"2023-06-13"}]'
