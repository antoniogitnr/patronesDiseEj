from typing import List

class CityIterator:
    def __init__(self, city: List[str]):
        self._city = city
        self._index = 0

    def __next__(self):
        if self._index >= len(self._city):
            raise StopIteration()

        value = self._city[self._index]
        self._index += 1
        return value

class CityTour:
    def __init__(self):
        self._city = []

    def add_landmark(self, landmark: str):
        self._city.append(landmark)

    def __iter__(self):
        return CityIterator(self._city)

if __name__ == "__main__":
    rome_tour = CityTour()
    rome_tour.add_landmark("Coliseo")
    rome_tour.add_landmark("Fontana di Trevi")
    rome_tour.add_landmark("Plaza de España")
    rome_tour.add_landmark("Vaticano")

    print("Recorrido por Roma:")
    for landmark in rome_tour:
        print(landmark)