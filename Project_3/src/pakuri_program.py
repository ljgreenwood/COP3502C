# Display a welcome message
# Prompt for / read pakudex capacity
# Display the menu
# Prompt for input

import sys
from pakudex import Pakudex


class Program:
    def __init__(self):
        self.pakudex = Pakudex()
        pass

    def menu(self):
        print("Welcome to Pakudex: Tracker Extraordinaire!")
        capacity = int(input("Enter max capacity of the Pakudex: "))
        print(f"The Pakudex can hold {capacity} species of Pakuri.")
        action = int(input("What would you like to do? "))
        print(
            """Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
"""
        )
        pass

    def get_input(self):
        pass

    def run(self):
        pass


def main():
    program = Program()
    program.run()
    print(sys.argv)  # command line arguments ???
