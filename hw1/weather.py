class Weather:

    def __init__(self, wind_speed):
        self.__wind_speed = wind_speed

    @property
    def wind_speed(self):
        return self.__wind_speed
