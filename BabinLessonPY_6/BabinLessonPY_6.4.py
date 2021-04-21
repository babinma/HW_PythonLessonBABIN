class Car:
    def __init__(self, name,speed,color,police):
        self.name = name
        self.speed = int(speed)
        self.color = color
        self.police = police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction == ">" or direction == "<":
            if direction == ">":
                print(f'{self.name} повернула направо')
            else:
                print(f'{self.name} повернула налево')
        else:
            print(f'{self.name}  едет прямо')

    def showspeed(self):
        if self.speed <= 20:
            print(f'Скорость {self.speed } км. Едете слишком медленно, созадете')
        if speed <= 40 and self.speed  > 20:
            print(f'Скорость {self.speed } км .Можно побыстрее')
        if self.speed < 80 and self.speed > 40:
            print(f'Скорость {self.speed } км.нормальная скорость')

class TownCar(Car):
    number_reg = 77
    def __init__(self, name, speed, color, police):
        super().__init__(name, speed, color, police)
    def showspeed(self):
        if self.speed  <= 20:
            print(f'Скорость {self.speed } км. Едете слишком медленно, созадаете пробку')
        if self.speed  <= 40 and self.speed  > 20:
            print(f'Скорость {self.speed } км .Можно побыстрее')
        if self.speed  > 60 and self.speed  > 20:
            print(f'Скорость {self.speed } км .Скорость слишком высокая')
        if self.speed <=60 and self.speed > 40:
            print(f'Скорость {self.speed } км.нормальная скорость')

class SportCar(Car):
    def __init__(self, name, speed, color, police):
        super().__init__(name, speed, color, police)
        self.color = "У спортивной машины цвет всегда красный"
class WorkCar(Car):
    def __init__(self, name, speed, color, police):
        super().__init__(name, speed, color, police)
    def showspeed(self, ):
        if self.speed <= 20:
            print(f'Скорость {self.speed } км. Едете слишком медленно, созадете')
        if self.speed > 40:
            print(f'Скорость {self.speed } км .Скорость для такой машины слишком высокая')
        if self.speed <=40 and self.speed > 20:
            print(f'Скорость {self.speed } км.нормальная скорость')
class PoliceCar(Car):
    def __init__(self, name, speed, color, police):
        super().__init__(name, speed, color, police)
    def showspeed(self):
        print(f'У полицейских всегда правильная скорость')
    def migalka(self):
        n=0
        while n <5:
            print("Красный")
            time.sleep(1)
            print("Синий")
            time.sleep(1)
            n +=1

Mazda = TownCar("Мазда", 60, "Белый", False)
MAZ = WorkCar("МАЗ", 70, "Синий",False)
Ferrari = SportCar("Феррари", 200, "Белый",False)
Reno= PoliceCar("Рено логан", 10, "Фиолетывый", True)

print(f'Марка машины {Mazda.name}')
print(f'Цвет Мазды {Mazda.color}')
Mazda.showspeed()
print(f'Номер региона {Mazda.number_reg}')
Mazda.turn("<")
print("\n")
print(f'Цвет МАЗа {MAZ.color}')
MAZ.showspeed()
MAZ.turn(">")
print("\n")
print(Ferrari.color)
Ferrari.turn("")
print("\n")
print(f'Марка полицейской машины {Reno.name}')
Reno.turn("")
Reno.showspeed()
print(f'Истинно ли то что Рено полицейская машиан - {Reno.police}!')
