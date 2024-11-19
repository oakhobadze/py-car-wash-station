class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center != 0:
            return round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating /
                         self.distance_from_city_center, 1)
        else:
            return 0.0

    def serve_cars(self, cars: list) -> float:
        res = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                res.append(self.calculate_washing_price(car))
                self.wash_single_car(car)

        return sum(res)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        new_mark = round((self.average_rating * self.count_of_ratings + mark) / (self.count_of_ratings + 1), 1)
        self.average_rating = new_mark
        self.count_of_ratings += 1
