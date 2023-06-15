from django.contrib.auth import login
from rest_framework import generics
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import *
from .serializers import *
from RMS.models.RestaurantWorker import RestaurantWorker, RestaurantAvailability
from MG_RMS import settings
from .serializers import RestaurantWorkerSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


class WorkerLoginView(KnoxLoginView):
    permission_classes = [AllowAny]

    def get_post_response_data(self, request, token, instance):

        worker = RestaurantWorker.objects.get(user=request.user)

        data = {
            'access_token': token,
            'token_type': settings.REST_KNOX['AUTH_HEADER_PREFIX'],
            'expires_at': self.format_expiry_datetime(instance.expiry),
            'user': {
                'associated_id': worker.id,
                'username': worker.user.username,
                'roles': worker.roles,
                'email': worker.user.email,
                'disabled': worker.disabled
            }
        }

        return data

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(WorkerLoginView, self).post(request, format=None)


class CurrentRestaurantWorkerView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantWorkerSerializer
    queryset = RestaurantWorker.objects.filter(id=1)


class RestaurantMenuEntryListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantMenuEntryPolymorphicSerializer
    queryset = RestaurantMenuEntry.objects.all()


# TODO: status 409
class RestaurantMenuEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantMenuEntryPolymorphicSerializer
    queryset = RestaurantMenuEntry.objects.all()


class RestaurantTableListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTableSerializer
    queryset = RestaurantTable.objects.all()


class RestaurantTablePropertyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTablePropertySerializer
    queryset = RestaurantTableProperty.objects.all()


class RestaurantTableBookingView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTableBookingSerializer
    queryset = RestaurantTableBooking.objects.all()


class StartEndHoursView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StartEndHoursSerializer
    queryset = StartEndHours.objects.all()
