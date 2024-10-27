import random


def game():
    print("Добро пожаловать в Космическую игру!")
    print("Вы - капитан корабля, уклоняющегося от астероидов.")
    print("Ваша цель - выжить как можно дольше!\n")

    ship_position = 5
    score = 0
    game_over = False

    while not game_over:
        asteroid_position = random.randint(1, 10)
        print("\nАстероид на позиции:", asteroid_position)
        print("Ваш корабль на позиции:", ship_position)

        move = input("Нажмите 'L' чтобы двинуться влево, 'R' чтобы двинуться вправо: ").lower()
        if move == "l" and ship_position > 1:
            ship_position -= 1
        elif move == "r" and ship_position < 10:
            ship_position += 1

        if ship_position == asteroid_position:
            print("Вы столкнулись с астероидом! Игра окончена.")
            game_over = True
        else:
            score += 1
            print("Вы успешно уклонились! Очки:", score)

    print("Ваш финальный счет:", score)


game()
