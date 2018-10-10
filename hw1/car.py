class Car:

    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }

    def __init__(self, name):
        self.name = name

    @property
    def max_speed(self):
        return self.CAR_SPECS[self.name]['max_speed']

    @property
    def drag_coef(self):
        return self.CAR_SPECS[self.name]['drag_coef']

    @property
    def time_to_max(self):
        return self.CAR_SPECS[self.name]['time_to_max']
