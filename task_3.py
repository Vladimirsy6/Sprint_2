class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total

# Примеры вызовов
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))  # 91

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))  # 5.0

total_points = TotalPoints()
print(total_points.get_points_for_place(10))        # 91
print(total_points.get_points_for_meters(10))       # 5.0
print(total_points.get_total_points(100, 10))       # 91 + 50.0 = 141.0