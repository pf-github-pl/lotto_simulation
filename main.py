"""Simulate lotto lottery results"""

from random import sample
from math import ceil


def draw(numbers):
    """Return a set of 6 unique numbers from given sequence"""
    return set(sample(numbers, k=6))


def compare_numbers(my_lucky_numbers: set, drawing_algorithm):
    """Compare two sets and return boolean"""
    return bool(my_lucky_numbers == drawing_algorithm)


def calculate_time(weekly_frequency, draws):
    """Calculate time in years, months, weeks and days assuming given weekly frequency"""
    days = draws / weekly_frequency * 7
    years_rem = int(days // 365)
    months_rem = int(days % 365 // 30)
    weeks_rem = int(days % 365 % 30 // 7)
    days_rem = int(ceil(days % 365 % 30 % 7))
    return f'{years_rem} lat, {months_rem} miesięcy, {weeks_rem} tygodni, {days_rem} dni'


def show_result(prize, cost, draws, weekly_frequency):
    """Print simulation results"""
    total_cost = cost * draws

    congrats = f'Brawo, wygrałeś {prize:,.0f} PLN w {draws:,.0f} losowaniach)\n'
    costs = f'Koszt zakładów wyniósł {total_cost:,.0f} PLN\n'
    result = f'Twój wynik to: {prize-total_cost:,.0f} PLN\n'
    time = f"Wygrana zajęła Ci {calculate_time(weekly_frequency, draws)}."

    return congrats + costs + result + time


def simulate():
    """Run lotto lottery simulation"""
    numbers = range(1, 50)
    my_lucky_numbers = {13, 8, 4, 34, 26, 44}
    prize = 8000000
    cost = 3
    weekly_frequency = 3
    draws = 0
    result = False

    print(f'Moje szczęśliwe liczby to: {sorted(list(my_lucky_numbers))}')

    while result is not True:
        draws += 1
        result = compare_numbers(my_lucky_numbers, draw(numbers))

    print(show_result(prize, cost, draws, weekly_frequency))


if __name__ == "__main__":
    simulate()
