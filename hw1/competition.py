from random import randint
from typing import List

from hw1.car import Car


class Competition:

    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self, distance):
        self.distance = distance

    def start(self, cars: List[Car], wind_speed):
        for car in cars:
            competitor_time = 0

            for distance in range(self.distance):
                _wind_speed = randint(0, wind_speed)

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > _wind_speed:
                        _speed -= (car.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (car.name, competitor_time))
