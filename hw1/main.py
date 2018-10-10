from hw1.car import Car
from hw1.weather import Weather
from hw1.competition import Competition

car_name = ('ferrary', 'bugatti', 'toyota', 'lada', 'sx4')
cars = [Car(name) for name in car_name]
weather = Weather(wind_speed=5)
competition = Competition(distance=10000)


if __name__ == '__main__':
    competition.start(cars=cars, wind_speed=weather.wind_speed)
