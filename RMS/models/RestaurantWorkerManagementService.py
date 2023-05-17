from django.db import models

class RestaurantWorkerManagementService(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    availableDeliveryWorkerIds = models.CharField(max_length=255)

    def predictStaff(self, date):
        pass

    def getWorkers(self):
        return RestaurantWorker.objects.filter(restaurant=self.restaurant)

    def getAvailableDeliveryWorkerIds(self):
        return self.availableDeliveryWorkerIds.split(',')

    def updateRestaurantWorkers(self, workers):
        for worker in workers:
            worker.restaurant = self.restaurant
            worker.save()

    def removeRestaurantWorker(self, worker):
        worker.delete()

    def addOrUpdateRestaurantWorker(self, worker):
        worker.restaurant = self.restaurant
        worker.save()

    def addAvailableDeliveryWorkerId(self, id):
        available_ids = self.getAvailableDeliveryWorkerIds()
        available_ids.append(id)
        self.availableDeliveryWorkerIds = ','.join(available_ids)
        self.save()

    def removeAvailableDeliveryWorkerId(self, id):
        available_ids = self.getAvailableDeliveryWorkerIds()
        if id in available_ids:
            available_ids.remove(id)
            self.availableDeliveryWorkerIds = ','.join(available_ids)
            self.save()

