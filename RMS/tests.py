from django.test import TestCase
from django.core.exceptions import ValidationError
from .models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from .models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from decimal import Decimal


class DishRestaurantMenuEntryTestCase(TestCase):
    def setUp(self):
        eggs = DishRestaurantMenuEntry.objects.create(name='Eggs Benedict',
                                                      price=Decimal('29.99'),
                                                      stage=DishRestaurantMenuEntry.DishStage.MAIN_COURSE,
                                                      weight=Decimal('0.3'))
        toast = DishRestaurantMenuEntry.objects.create(name='Toast with ham',
                                                       price=Decimal('9.99'),
                                                       stage=DishRestaurantMenuEntry.DishStage.MAIN_COURSE,
                                                       weight=Decimal('0.1'))
        eggs.full_clean()
        eggs.save()
        toast.full_clean()
        toast.save()

    def test_create_clean_and_save(self):
        crepes = DishRestaurantMenuEntry.objects.create(name='Crepes',
                                                        price=Decimal('5.99'),
                                                        stage=DishRestaurantMenuEntry.DishStage.DESSERT,
                                                        weight='0.24')
        crepes.full_clean()
        crepes.save()

        crepes_read = DishRestaurantMenuEntry.objects.get(name='Crepes')
        self.assertEqual(crepes_read.price, Decimal('5.99'))
        self.assertEqual(crepes_read.stage, DishRestaurantMenuEntry.DishStage.DESSERT)
        self.assertEqual(crepes_read.weight, Decimal('0.24'))

    def test_assign_nonexistent_DishStage(self):
        eggs = DishRestaurantMenuEntry.objects.get(name='Eggs Benedict')
        eggs.stage = 6

        with self.assertRaises(ValidationError) as cm:
            eggs.full_clean()

        ex = cm.exception
        self.assertIn('stage', ex.error_dict)
        stage_exceptions = ex.error_dict['stage']
        self.assertEqual(1, len(stage_exceptions))
        stage_exception = stage_exceptions[0]
        self.assertEqual('Value %(value)r is not a valid choice.', stage_exception.message)
        self.assertIn('value', stage_exception.args[2])
        self.assertEqual(6, stage_exception.args[2]['value'])

    def test_assign_negative_price(self):
        toast = DishRestaurantMenuEntry.objects.get(name='Toast with ham')
        toast.price = Decimal('-2.44')

        with self.assertRaises(ValidationError) as cm:
            toast.full_clean()

        ex = cm.exception
        self.assertIn('price', ex.error_dict)
        price_exceptions = ex.error_dict['price']
        self.assertEqual(1, len(price_exceptions))
        price_exception = price_exceptions[0]
        self.assertEqual('Price cannot be negative.', price_exception.message)

    def test_assign_negative_weight(self):
        toast = DishRestaurantMenuEntry.objects.get(name='Toast with ham')
        toast.weight = Decimal('-0.888')

        with self.assertRaises(ValidationError) as cm:
            toast.full_clean()

        ex = cm.exception
        self.assertIn('weight', ex.error_dict)
        weight_exceptions = ex.error_dict['weight']
        self.assertEqual(1, len(weight_exceptions))
        weight_exception = weight_exceptions[0]
        self.assertEqual('Weight cannot be negative.', weight_exception.message)

    def test_create_dish_with_empty_name(self):
        empty_name_dish = DishRestaurantMenuEntry.objects.create(name='',
                                                                 price=Decimal('9.99'),
                                                                 stage=DishRestaurantMenuEntry.DishStage.MAIN_COURSE,
                                                                 weight=Decimal('4.13'))
        with self.assertRaises(ValidationError) as cm:
            empty_name_dish.full_clean()

        ex = cm.exception
        self.assertIn('name', ex.error_dict)
        name_exceptions = ex.error_dict['name']
        self.assertEqual(1, len(name_exceptions))
        name_exception = name_exceptions[0]
        self.assertEqual('This field cannot be blank.', name_exception.message)


class DrinkRestaurantMenuEntryTestCase(TestCase):
    def setUp(self):
        coke = DrinkRestaurantMenuEntry.objects.create(name='Coca Cola',
                                                       price=Decimal('2.99'),
                                                       volume=Decimal('0.33'))
        booze = DrinkRestaurantMenuEntry.objects.create(name='Heineken',
                                                        price=Decimal('5.40'),
                                                        contains_alcohol=True,
                                                        volume=Decimal('0.5'))
        coke.full_clean()
        coke.save()
        booze.full_clean()
        booze.save()

    def test_create_clean_and_save(self):

        booze_read = DrinkRestaurantMenuEntry.objects.get(name='Heineken')
        self.assertEqual(booze_read.price, Decimal('5.40'))
        self.assertEqual(booze_read.contains_alcohol, True)
        self.assertEqual(booze_read.volume, Decimal('0.5'))

        coke_read = DrinkRestaurantMenuEntry.objects.get(name='Coca Cola')
        self.assertEqual(coke_read.price, Decimal('2.99'))
        self.assertEqual(coke_read.contains_alcohol, False)
        self.assertEqual(coke_read.volume, Decimal('0.33'))

    def test_assign_negative_price(self):
        coke = DrinkRestaurantMenuEntry.objects.get(name='Coca Cola')
        coke.price = Decimal('-2.44')

        with self.assertRaises(ValidationError) as cm:
            coke.full_clean()

        ex = cm.exception
        self.assertIn('price', ex.error_dict)
        price_exceptions = ex.error_dict['price']
        self.assertEqual(1, len(price_exceptions))
        price_exception = price_exceptions[0]
        self.assertEqual('Price cannot be negative.', price_exception.message)

    def test_assign_negative_volume(self):
        booze = DrinkRestaurantMenuEntry.objects.get(name='Heineken')
        booze.volume = Decimal('-0.888')

        with self.assertRaises(ValidationError) as cm:
            booze.full_clean()

        ex = cm.exception
        self.assertIn('volume', ex.error_dict)
        volume_exceptions = ex.error_dict['volume']
        self.assertEqual(1, len(volume_exceptions))
        volume_exception = volume_exceptions[0]
        self.assertEqual('Volume cannot be negative.', volume_exception.message)

    def test_create_drink_with_single_letter_name(self):
        empty_name_drink = DrinkRestaurantMenuEntry.objects.create(name='A',
                                                                   price=Decimal('99.40'),
                                                                   contains_alcohol=False,
                                                                   volume=Decimal('0.5'))

        with self.assertRaises(ValidationError) as cm:
            empty_name_drink.full_clean()

        ex = cm.exception
        self.assertIn('name', ex.error_dict)
        name_exceptions = ex.error_dict['name']
        self.assertEqual(1, len(name_exceptions))
        name_exception = name_exceptions[0]
        self.assertEqual('Name must be at least 2 characters long.', name_exception.message)
