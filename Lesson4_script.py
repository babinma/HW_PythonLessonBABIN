from sys import argv

script_name, time, rate_per_hour, bonus = argv
time1 = int(time)
rate_per_hour2 = int(rate_per_hour)
bonus3 = int(bonus)
salary_fact = (time1 * rate_per_hour2) + bonus3
print(f'Отработанное время в часах: {time1}, Ставка долларов в час:  {rate_per_hour2}, Бонус долларов: {bonus3}')
print(f'Расчет вознаграждения равен: {salary_fact} долларов')