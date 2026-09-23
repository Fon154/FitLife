# Константы
WATER_PER_KG = 30
ML_IN_L = 1000

# Знакомство
print("Привет!")
user_name = input("Введите Ваше имя: ")
user_age = int(input("Введите Ваш возраст: "))

# Сбор данных
user_weight = float(input("Введите Ваш вес (в кг): "))
user_height = float(input("Введите Ваш рост (в метрах, например 1.75): "))

# Рассчеты ИМТ
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды
water_ml = user_weight * WATER_PER_KG
water_needed = water_ml / ML_IN_L
water_needed = round(water_needed, 3)

# Вывод результата
print(f'\nОтчет для пользователя: {user_name}')
print(f'Возраст: {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день')

print("Расчет окончен. Будьте здоровы!")
