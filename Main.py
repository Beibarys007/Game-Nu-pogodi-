import random
import time

# Определяем количество лотков и количество яиц, которые нужно поймать для победы
NUM_SLOTS = 4
NUM_EGGS_TO_WIN = 10

# Задаем скорость движения яиц
INITIAL_SPEED = 1.0
SPEED_INCREASE = 0.1

# Инициализируем переменные для отслеживания счета и времени
score = 0
start_time = time.time()

# Функция для печати текущего состояния игры
def print_game_state(slots, egg_position):
    print("-" * 30)
    print("Score:", score)
    for i in range(NUM_SLOTS):
        if egg_position == i:
            print("[E]", end="")
        else:
            print("[ ]", end="")
    print("")
    print(" ".join([str(x) for x in slots]))

# Функция для получения ввода от пользователя
def get_input():
    while True:
        user_input = input("Введите номер лотка (от 1 до " + str(NUM_SLOTS) + "): ")
        try:
            slot_number = int(user_input)
            if slot_number < 1 or slot_number > NUM_SLOTS:
                raise ValueError
            break
        except ValueError:
            print("Ошибка: введите число от 1 до " + str(NUM_SLOTS))
    return slot_number - 1

# Инициализируем массив лотков
slots = [0] * NUM_SLOTS

# Запускаем игру
egg_position = None
speed = INITIAL_SPEED
while score < NUM_EGGS_TO_WIN:
    # Двигаем яйцо вниз, если оно уже есть на поле
    if egg_position is not None:
        slots[egg_position] = 0
        egg_position += 1
        if egg_position == NUM_SLOTS:
            egg_position = None
    # Добавляем новое яйцо в случайном лотке
    if egg_position is None:
        egg_position = random.randint(0, NUM_SLOTS - 1)
    slots[egg_position] = 1
    # Печатаем текущее состояние игры и получаем ввод от пользователя
    print_game_state(slots, egg_position)
    slot_number = get_input()
    # Проверяем, поймал ли игрок яйцо
    if slots[slot_number] == 1:
        print("Поймано!")
        score += 1
        speed += SPEED_INCREASE
        time.sleep(0.5)
    else:
        print("Промах!")
    # Увеличиваем скорость движения яиц
    time.sleep(1.0 / speed)

# Игра завершена, печатаем результаты
end_time = time.time()
print("Вы поймали", NUM_EGGS_TO_WIN, "яиц за", int(end_time - start_time), "секунд.")
