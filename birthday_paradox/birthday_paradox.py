from datetime import date, timedelta
from random import randint

class BirthdayParadox:
    MAX_SIMULATION_COUNT = 100_000

    def __init__(self):
        self.birthday_count = 0
        self.birthdays = []
        self.simulation_count = 0
        self.results = 0
        self.base_date = date(2001, 1, 1)

    def get_user_input(self):
        user_input = input('How many birthdays shall I generate? (Max 100) \n> ')

        if user_input.isdecimal() and (0 < int(user_input) <= 100):
            self.birthday_count = int(user_input)
            self.__execute()
        else:
            print('Please enter a number from 1 to 100\n')
            return self.get_user_input()

    def __execute(self):
        self.__populate_birthdays()
        print(f'Here are {self.birthday_count} birthdays:\n')
        print(f"{', '.join(self.birthdays)}\n")

        matched_birthday = self.__get_matched_birthdays()
        if matched_birthday:
            print(f"In this simulation, multiple people have a birthday on {matched_birthday}")

        print(f'Generating {self.birthday_count} random birthdays 100,000 times...')
        input('Press Enter to begin... \n')

        for _ in range(BirthdayParadox.MAX_SIMULATION_COUNT):
            self.__run_simulation()

        self.__print_result()

    def __run_simulation(self):
        if self.simulation_count == BirthdayParadox.MAX_SIMULATION_COUNT:
            print(f'{self.simulation_count} simulations run.')
            return -1

        if self.simulation_count % 10_000 == 0:
            print(f'{self.simulation_count} simulations run...')

        self.simulation_count += 1
        self.__populate_birthdays()
        self.__get_matched_birthdays()

    def __get_matched_birthdays(self):
        if len(self.birthdays) == len(set(self.birthdays)):
            return None

        birthdays: dict = {}
        for birthday in self.birthdays:
            birthdays[birthday] = birthdays.get(birthday, 0) + 1

        duplicated_birthdays: dict = {k:v for (k, v) in birthdays.items() if v > 1}
        self.results += 1
        return list(duplicated_birthdays.keys())[0]

    def __populate_birthdays(self):
        self.birthdays = [
            (self.base_date + timedelta(randint(0, 364))).strftime('%b %-d') for _ in range(self.birthday_count)
        ]

    def __print_result(self):
        matched_birthday_percent = self.results / self.simulation_count * 100

        print(f'Out of 100,000 simulations of {self.birthday_count} people, there was a\n')
        print(f'matching birthday in that group {self.results} times. This means\n')
        print(f'that {self.birthday_count} people have a {matched_birthday_percent} % chance of\n')
        print(f'having a matching birthday in their group.\n')
        print(f"That's probably more than you would think!")

if __name__ == "__main__":
    print('''Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
        The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.
        (It's not actually a paradox, it's just a surprising result.)
        ''')
    birthday_paradox = BirthdayParadox()
    birthday_paradox.get_user_input()
