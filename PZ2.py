# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах: "))

sek = time % 60
minute = (time - sek) % 3600 // 60
hour = (time - sek - minute) % (3600 * 24) // 3600
day = (time - sek - minute - hour) // (24 * 3600)

result = f'Time is: {day}:{hour:02}:{minute:02}:{sek:02}'
print(result)
