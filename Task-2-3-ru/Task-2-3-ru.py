# Инициализация переменных
direction = 0  # 0: направление неизвестно, 1: вверх, -1: вниз
changes = 0    # Счетчик смен направления
new_direction = direction  # Новое направление
# Считываем первый этаж
prev = int(input())
b_done = (prev == 0)  # флаговая переменная условие выхода из цикла
while not b_done:
    current = int(input())  # Вводим остальные этажи
    b_done = (current == 0)  # Выходим из цикла, если введен 0
    # Если этажи совпадают, направление не меняется,
    # просто пропускаем
    if not b_done and current != prev:
        # Определяем новое текущее направление
        # между prev и current
        new_direction = 1
        if current > prev:
            new_direction = -1
    # Если до этого направление уже было известно (не 0)
    # и оно не совпадает с новым направлением, значит произошла смена
    if not b_done and direction != 0 and new_direction != direction:
        changes += 1
    # Обновляем историю для следующего шага
    direction = new_direction
    prev = current

print(f"Количество смен направления лифтом: {changes}")
