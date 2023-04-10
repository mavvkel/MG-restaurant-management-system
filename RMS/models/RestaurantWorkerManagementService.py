class RestaurantWorkerManagementService:
    def __init__(self, restaurant):
        self.__restaurant = restaurant
        self.__availableDeliveryWorkerIds = []

    def predictStaff(self, date):
        # Method body
        pass

    def getWorkers(self):
        return self.__restaurant.getWorkers()

    def getAvailableDeliveryWorkerIds(self):
        return self.__availableDeliveryWorkerIds

    def updateRestaurantWorkers(self, workers):
        self.__restaurant.setWorkers(workers)

    def removeRestaurantWorker(self, worker):
        self.__restaurant.removeWorker(worker)

    def addOrUpdateRestaurantWorker(self, worker):
        self.__restaurant.addOrUpdateWorker(worker)

    def addAvailableDeliveryWorkerId(self, id):
        self.__availableDeliveryWorkerIds.append(id)

    def removeAvailableDeliveryWorkerId(self, id):
        self.__availableDeliveryWorkerIds.remove(id)


