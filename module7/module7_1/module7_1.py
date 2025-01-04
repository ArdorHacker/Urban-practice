class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}\n"

class Shop:
    repeat = False

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        file_str = file.read()
        file.close()
        return file_str

    def add(self, *products):
        for i in products:
            if self.get_products().find(i.name) == -1:
                file = open(self.__file_name, "a")
                file.write(f"{i}")
                file.close()

            else:
                file_lst = self.get_products().split("\n")
                del file_lst[-1]

                file = open(self.__file_name, "w")
                file.write("")
                file.close()

                for j in file_lst:
                    j_lst = j.split(", ")
                    if j_lst[0] == i.name:
                        j_lst[1] = str(float(j_lst[1]) + i.weight)
                        print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {j_lst[1]}')

                    file = open(self.__file_name, "a")
                    file.write(f"{j_lst[0]}, {j_lst[1]}, {j_lst[2]}\n")
                    file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())