import math


class Figure:
    sides_count = None
    useful_sides = None

    def __init__(self, color, *sides, filled=False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

        self.set_color(color[0], color[1], color[2])
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, c1, c2, c3):
        colors = [c1, c2, c3]
        for color in colors:
            if not (0 <= color <= 255):
                return False
        return True

    def set_color(self, c1, c2, c3):
        if self.__is_valid_color(c1, c2, c3):
            self.__color = [c1, c2, c3]

    def __is_valid_sides(self, sides):
        if len(sides) == self.useful_sides and (0 not in sides):
            return True
        return False

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)

            if self.useful_sides == 1:
                list_ = []
                for i in range(self.sides_count):
                    list_.append(self.__sides[0])
                self.__sides = list_
                del list_


    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.__sides is not None:
            return sum(self.__sides)
        else:
            return 0


class Circle(Figure):
    sides_count = 1
    useful_sides = 1

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self.__radius = len(self) / 2 * math.pi

    def get_square(self):
        print(round(math.pi * self.__radius ** 2, 2))

class Cube(Figure):
    sides_count = 12
    useful_sides = 1

    def __init__(self, *args):
        Figure.__init__(self, *args)

    def get_volume(self):
        return (len(self) // self.sides_count) ** 3


class Triangle(Figure):
    sides_count = 3
    useful_sides = 3

    def __init__(self, *args):
        Figure.__init__(self, *args)

    def get_square(self):
        p = len(self) / 2

        if p == 0:
            return None

        a, b, c = self.__sides
        v = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

        return round(v, 2)


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())