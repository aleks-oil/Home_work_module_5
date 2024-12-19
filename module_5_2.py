
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nfloors = number_of_floors

    def go_to (self, new_floor):
        if 1 < new_floor < self.nfloors:
            for i in range(1, new_floor+1):
                print(i)
            else:
                print('Такого этажа не существует')

    def __len__(self):
        return self.nfloors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.nfloors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))