# Константы
WATER_PER_KG = 30
ML_IN_L = 1000

# Знакомство
print("Привет!")


# Имя
while True:
    user_name = input("Введите Ваше имя: ").strip()
    if user_name:
        break
    print("Имя не может быть пустым")


# Возраст
while True:
    try:
        user_age = int(input("Введите Ваш возраст (например, 27): "))
        if user_age >= 0:
            break
        print("Возраст не может быть отрицательным")
    except ValueError:
        print("Введите целое число")


# Вес
while True:
    try:
        user_weight = float(input("Введите Ваш вес (в кг): "))
        if user_weight > 0:
            break
        print("Вес должен быть больше нуля")
    except ValueError:
        print("Введите число")


# Рост
while True:
    try:
        user_height = float(input("Введите Ваш рост в метрах, "
                                  "(например 1.75): "))
        if user_height > 0:
            break
        print("Рост должен быть больше нуля")
    except ValueError:
        print("Введите число")


# Рассчеты ИМТ
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды
water_ml = user_weight * WATER_PER_KG
water_needed = round(water_ml / ML_IN_L, 3)

# Вывод результата
print(f'\n\nОтчет для пользователя: {user_name}')
print(f'Возраст: {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день\n')

print("Расчет окончен. Будьте здоровы!")
