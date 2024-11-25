#работа со словарём

my_dict = {"Egor": 1999, "Danil": 2002, "Dima": 2015}
print(my_dict)
print(my_dict["Danil"])
print(my_dict.get("danil"))
my_dict.update({"Gleb": 2006,
                "Masha": 2020})
a = my_dict.pop("Egor")
print(a)
print(my_dict)

#работа со множеством
print("\n", "#"*20, "\n")

my_set = {5, "Apple", True}
print(my_set)
my_set.add(10.4)
my_set.add("Hello")
my_set.remove(5)
print(my_set)
