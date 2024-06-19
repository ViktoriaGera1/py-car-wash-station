class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                price = self.calculate_washing_price(i)
                self.wash_single_car(i)
                income += price
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        total = self.count_of_ratings * self.average_rating
        total += rate
        self.count_of_ratings += 1
        self.average_rating = total / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)
