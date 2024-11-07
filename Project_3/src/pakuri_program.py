from pakudex import Pakudex


class Program:
    # Prompt for input
    def __init__(self):
        self.pakudex = Pakudex()
        pass

    def menu(self):
        # Display the menu
        print(
            """
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
"""
        )

    def get_int_input(self, msg: str, err_msg: str = "Error") -> int:
        while True:
            try:
                temp = int(input(msg))  # No default value
                break
            except:
                print(err_msg)  # Error by default
        return temp

    def run(self):
        # Display a welcome message
        print("Welcome to Pakudex: Tracker Extraordinaire!")
        # Prompt for / read pakudex capacity
        self.pakudex.capacity = self.get_int_input(
            msg="Enter max capacity of the Pakudex: ",
            err_msg="Please enter a valid size.",
        )
        print(f"The Pakudex can hold {self.pakudex.capacity} species of Pakuri.")
        # Display menu
        while True:
            self.menu()
            # Input action (selection)
            action = self.get_int_input(
                msg="What would you like to do? ",
                err_msg="Unrecognized menu selection!",
            )
            print(action)


def main():
    program = Program()
    program.run()


if __name__ == "__main__":
    main()
