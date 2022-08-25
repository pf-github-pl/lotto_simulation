"""Simulate lotto lottery results"""

from random import randint


def draw():
    """Return a set of 6 numbers from range 1-49"""
    drawn_numbers = set()

    while len(drawn_numbers) < 6:
        number = randint(1, 50)
        if number not in drawn_numbers:
            drawn_numbers.add(number)
    return drawn_numbers


def compare_numbers(my_lucky_numbers: set, drawn_numbers: set):
    """Compare two sets and return boolean"""
    return bool(my_lucky_numbers == drawn_numbers)


def calculate_time(weekly_frequency, draw_number):
    """Calculate time in years assuming some weekly frequency"""
    weeks = draw_number / weekly_frequency
    years = round(weeks / 52, 2)
    return f"Wygrana zajęła Ci {years:,.2f} lat."


def show_result(prize, cost, draw_number, weekly_frequency):
    """Print simulation results"""
    total_cost = cost * draw_number

    congrats = f'Brawo, wygrałeś {prize:,.0f} PLN w {draw_number:,.0f} losowaniach)\n'
    costs = f'Koszt zakładów wyniósł {total_cost:,.0f} PLN\n'
    result = f'Twój wynik to: {prize-total_cost:,.0f} PLN\n'
    time = calculate_time(weekly_frequency, draw_number)

    return congrats + costs + result + time


def simulate():
    """Run lotto lottery simulation"""
    my_lucky_numbers = {13, 8, 4, 34, 26, 44}
    prize = 8000000
    cost = 3
    weekly_frequency = 3
    draw_number = 0
    result = False

    print(f'Moje szczęśliwe liczby to: {sorted(list(my_lucky_numbers))}')

    while result is not True:
        draw_number += 1
        drawn_numbers = draw()
        result = compare_numbers(my_lucky_numbers, drawn_numbers)

    print(show_result(prize, cost, draw_number, weekly_frequency))


if __name__ == "__main__":
    simulate()
