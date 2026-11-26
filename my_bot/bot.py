print("bot")

# CO-OP Football Manager

# Склад футбольної команди
team = {
    "Воротар": "Андрій",
    "Захисник": "Максим",
    "Півзахисник": "Олександр",
    "Нападник": "Дмитро"
}

# Бюджет клубу
budget = 1000000

# Головне меню
def menu():
    print("\n=== CO-OP FOOTBALL MANAGER ===")
    print("/team - Склад команди")
    print("/transfer - Трансфери")
    print("/match - Провести матч")
    print("/exit - Вийти")

# Перегляд складу
def show_team():
    print("\nСклад команди:")
    for position, player in team.items():
        print(position + ": " + player)

# Купівля футболіста
def transfer():
    global budget

    name = input("Введіть ім'я футболіста: ")
    price = 200000

    if name.strip() == "":
        print("Помилка: ім'я не може бути порожнім!")
    elif budget >= price:
        team["Новий гравець"] = name
        budget -= price
        print("Футболіста придбано!")
        print("Залишок бюджету:", budget)
    else:
        print("Недостатньо коштів!")

# Проведення матчу
def match():
    import random

    goals = random.randint(0, 5)
    opponent = random.randint(0, 5)

    print("\nРезультат матчу:")
    print("Наша команда:", goals)
    print("Суперник:", opponent)

    if goals > opponent:
        print("Перемога!")
    elif goals < opponent:
        print("Поразка!")
    else:
        print("Нічия!")

# Основний цикл бота
while True:
    menu()
    command = input("\nВведіть команду: ").strip().lower()

    if command == "/team":
        show_team()

    elif command == "/transfer":
        transfer()

    elif command == "/match":
        match()

    elif command == "/exit":
        print("Дякуємо за гру!")
        break

    else:
        print("Невідома команда! Спробуйте ще раз.")
