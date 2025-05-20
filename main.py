def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)


# blad w formie return 0, powinno byc return 1


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)


assert factorial2(0) == 1
assert factorial2(3) == 6
assert factorial2(5) == 120


def get_grades():
    return [5, 4, "3", 2, 1]


def calculate_average(grades):
    return sum(grades) / len(grades)


# blad tutaj, dodac kontrole czy ocena jest liczba


def calculate_average2(grades):
    sum = 0
    for grade in grades:
        sum += int(grade)
    return sum / len(grades)


def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"


def show_result():
    grades = get_grades()
    avg = calculate_average2(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = int(hp)

    def take_damage(self, amount):
        self.hp = max(0, int(self.hp - amount))


class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = int(self.strength * 1.5)
        target.take_damage(damage)


class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")


def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)  # Powinien wypisać "Not enough mana!"
    print("End:", w.hp, m.hp)

    # Testy (asercje)
    assert m.hp == 45
    assert w.hp == 50
    assert m.mana == 0


simulate_battle()
