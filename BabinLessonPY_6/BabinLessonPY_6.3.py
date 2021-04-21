class Worker:
    def __init__(self):
        self.name = input('Укажите имя нового сотрудника: ')
        self.surname = input('Укажите фамилию сотрудника: ')
        self.position = input('Укажите должность сотрудника: ')
        wage = int(input('Укажите оклад сотрудника: '))
        bonus = int(input('Укажите премию сотрудника: '))
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        self.fio = self.name + " " + self.surname
        print(f'Полное имя сотрудника: {self.fio}')
    def get_total_income(self):
        self.dohod = int(self._income.get("wage")+self._income.get("bonus"))
        print(f'Полный доход сотрудника {self.dohod} рублей')

rabotnik1 = Position()
rabotnik1.get_full_name()
rabotnik1.get_total_income()
print(f'Должность сотрудника: {rabotnik1.position}')

rabotnik2 = Position()
rabotnik2.get_full_name()
rabotnik2.get_total_income()
print(f'Должность сотрудника: {rabotnik2.position}')