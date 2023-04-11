import RestaurantTableBooking
import RestaurantOrder


class StationaryRestaurantOrder(RestaurantOrder):
    tableBooking = RestaurantTableBooking
    customerComments = str

