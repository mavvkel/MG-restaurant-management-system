from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIRequestFactory
from rest_framework import status
from decimal import Decimal
import ast
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from api.views import RestaurantMenuEntryListView, RestaurantMenuEntryDetailView


class RestaurantMenuEntryListViewTests(TestCase):
    def setUp(self) -> None:
        DishRestaurantMenuEntry.objects.all().delete()
        self.assertEqual(DishRestaurantMenuEntry.objects.all().exists(), False)
        self.test_DishMenuEntry1 = DishRestaurantMenuEntry.objects.create(name='Eggs Benedict',
                                                                          price=Decimal('29.99'),
                                                                          stage=DishRestaurantMenuEntry.DishStage.MAIN_COURSE,
                                                                          weight=Decimal('0.3'))
        self.test_DishMenuEntry2 = DishRestaurantMenuEntry.objects.create(name='Toast with ham',
                                                                          price=Decimal('9.99'),
                                                                          stage=DishRestaurantMenuEntry.DishStage.STARTER,
                                                                          weight=Decimal('0.1'))

        self.test_user1 = User.objects.create(username='test_user1')
        self.test_user1.set_password('123')
        self.test_user1.save()
        self.assertEqual(len(User.objects.all()), 1)
        self.factory = APIRequestFactory()
        self.list_view = RestaurantMenuEntryListView.as_view()
        self.detail_view = RestaurantMenuEntryDetailView.as_view()

    def test_get_DishRestaurantMenuEntry_list(self):
        url = reverse('api:menu_entry_list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.test_user1)
        response = self.list_view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(ast.literal_eval(response.rendered_content.decode('utf-8'))), 2)
        self.assertContains(response, text='Eggs Benedict', count=1)
        self.assertContains(response, text='Toast with ham', count=1)

    def test_post_DishRestaurantMenuEntry_list(self):
        url = reverse('api:menu_entry_list')
        body = \
            {
                'name': 'Scrambled eggs',
                'price': '20.54',
                'stage': '2',
                'weight': '0.250'
            }
        request = self.factory.post(url, body, format='json')
        force_authenticate(request, user=self.test_user1)
        response = self.list_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        request = self.factory.get(url)
        force_authenticate(request, user=self.test_user1)
        response = self.list_view(request)
        self.assertContains(response, text='Scrambled eggs', count=1)
