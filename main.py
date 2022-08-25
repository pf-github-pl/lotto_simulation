from random import randint
import timeit

def simulate():

    my_lucky_numbers = sorted([13, 8, 4, 34, 26, 44])
    prize = 8000000
    cost = 3

    def draw():
        i = 0
        drawn_numbers = set()

        while len(drawn_numbers) < 6:
            number = randint(1, 49)
            if number not in drawn_numbers:
                drawn_numbers.add(number)
        if set(my_lucky_numbers) == drawn_numbers:
            return True

    i = 0
    result = False

    print(f'Moje szczęśliwe liczby to: {my_lucky_numbers}')

    while result is not True:
        i += 1
        result = draw()

    total_cost = i * cost
    print(f'Brawo, wygrałeś {prize:,.0f} PLN w {i:,.0f} losowaniach\nKoszt zakładów wyniósł {total_cost:,.0f} PLN\nTwój wynik to: {prize-total_cost:,.0f} PLN')


if __name__ == "__main__":
    simulate()