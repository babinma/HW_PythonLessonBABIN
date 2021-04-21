import time
import msvcrt
def timelight(d):
    for a in range(0, d):
        t = d-a
        print(f'{t} сек.')
        time.sleep(1)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 32:
                v = "exit"
                return v

class TrafficLight:
    mark = "Светофор"
    __color = ""
    def __init__(self):
        pass
    def running(self):
        timered = 7
        timeyellow = 2
        timegreen = 4
        zapusk = input("Запустить светофор(y/n)? ")
        if zapusk == "y":
            print("Для выключения светофора нажмите пробел!")
            while True:
                self.color = "ГОРИТ КРАСНЫЙ! Желтый загорится через:"
                print(self.color)
                v = timelight(timered)
                if v == "exit":
                    break
                self.color = "ГОРИТ ЖЕЛТЫЙ! Зеленый загорится через:"
                print(self.color)
                v = timelight(timeyellow)
                if v == "exit":
                    break
                self.color = "ГОРИТ ЗЕЛЕНЫЙ! Красный загорится через"
                print(self.color)
                v = timelight(timegreen)
                if v == "exit":
                    break
            print('Работа светофора завершена!')
        else:
            print("Помните! Перебегать дорогу в неположенном месте опасно!")

my_trafficLight = TrafficLight()
my_trafficLight.running()