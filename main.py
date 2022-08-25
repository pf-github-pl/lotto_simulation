from random import randint

def simulate():

    my_lucky_numbers = {13, 8, 4, 34, 26, 44}
    prize = 8000000
    cost = 3

    def draw():
        drawn_numbers = set()

        while len(drawn_numbers) < 6:
            number = randint(1, 49)
            if number not in drawn_numbers:
                drawn_numbers.add(number)
        if my_lucky_numbers == drawn_numbers:
            return True

    i = 0
    result = False

    print(f'Moje szczęśliwe liczby to: {sorted(list(my_lucky_numbers))}')

    while result is not True:
        i += 1
        result = draw()

    total_cost = i * cost
    print(f'Brawo, wygrałeś {prize:,.0f} PLN w {i:,.0f} losowaniach)')
    print(f'Koszt zakładów wyniósł {total_cost:,.0f} PLN')
    print(f'Twój wynik to: {prize-total_cost:,.0f} PLN')


if __name__ == "__main__":
    simulate()
