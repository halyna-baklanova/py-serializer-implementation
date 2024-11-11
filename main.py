from io import BytesIO

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    return serializer.data
