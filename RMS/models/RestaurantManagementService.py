class RestaurantManagementService:
    def __init__(self, restaurant):
        self.__restaurant = restaurant

    def getRestaurantManagerContactData(self):
        return self.__restaurant.getManager().getContactData()

    def getRestaurantMenu(self):
        return self.__restaurant.getMenu()

    def getRestaurantAvailability(self):
        return self.__restaurant.getAvailability()

    def updateRestaurantAvailability(self, availability):
        self.__restaurant.setAvailability(availability)

    def updateRestaurantMenu(self, menu):
        self.__restaurant.setMenu(menu)

    def addOrUpdateRestaurantMenuEntry(self, menuEntry):
        self.__restaurant.addOrUpdateMenuEntry(menuEntry)

    def removeRestaurantMenuEntry(self, menuEntry):
        self.__restaurant.removeMenu(menuEntry)

    def updateRestaurantTables(self, tables):
        self.__restaurant.setTables(tables)

    def addOrUpdateRestaurantTable(self, table):
        self.__restaurant.addOrUpdateTable(table)

    def removeRestaurantTable(self, table):
        self.__restaurant.removeTable(table)

    def use(self):
        # Method body
        pass
