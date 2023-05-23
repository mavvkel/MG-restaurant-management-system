from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIRequestFactory, APITestCase
from decimal import Decimal
from RMS.models.DishRestaurantMenuEntry import *
from RMS.models.DrinkRestaurantMenuEntry import *
from RMS.models.RestaurantMenuEntry import *
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
        Ensure unauthenticated POST method on /api/restaurant/menu endpoint is working.
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
