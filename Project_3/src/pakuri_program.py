from pakudex import Pakudex
# import logging

# logging.basicConfig(level=logging.DEBUG)

# TODO: Before submitting program... branch and check how ChatGPT would reformat this code! (still submit the original but learn from the reformatting)


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

    def run(self):
        # Display a welcome message
        print("Welcome to Pakudex: Tracker Extraordinaire!")
        # Prompt for / read pakudex capacity -> must return int so use get_int_input()
        while True:
            try:
                temp = int(
                    input("Enter max capacity of the Pakudex: ")
                )  #  if the entered type is incorrect,
                if temp < 1:
                    raise ValueError("Invalid Pakudex Size")
                # if no exceptions are raised above, set the capacity to the temp value
                self.pakudex.capacity = temp
                break  # exit loop for values
            except:  # catch :: all exceptions
                print("Please enter a valid size.")  # Error by default
        print(
            f"The Pakudex can hold {self.pakudex.capacity} species of Pakuri."
        )  # Print statement to show capacity of Pakudex
        # Display menu
        while True:
            self.menu()
            # Input action (selection) -> again must return int so use get_int_input()
            try:
                temp = int(input("What would you like to do? "))  # No default value
                if temp > 6 or temp < 1:
                    raise ValueError("Selections must be in range")
                action = temp
            except (
                ValueError
            ) as ve:  # Both the specified ValueError and the temp input ValueError may be raised
                print("Unrecognized menu selection!")
                # logging.debug(ve)
                continue  # restart loop without going through program logic
            # except Exception as e:
            #     logging.debug(e)
            # START ACTION SELECTION LOGIC!
            if action == 1:  # LIST PAKURI
                try:
                    result = self.pakudex.get_species_array()
                    assert (
                        result != None
                    )  # raise AssertionError if the program returns "None"
                    print("Pakuri In Pakudex: ")
                    for i in range(len(result)):
                        print(f"{i+1}. {result[i]}")
                except AssertionError:
                    print("No Pakuri in Pakudex yet!")
                except Exception as e:
                    print("Unknown Error: ", e)

            if action == 2:  # SHOW PAKURI
                try:
                    pakuri_sel = input("Enter the name of the species to display: ")
                    result = self.pakudex.get_stats(pakuri_sel)
                    assert isinstance(
                        result, list
                    ), "No Pakuri Found"  # Will raise an assertion error if the result is not a list
                    print(
                        f"Species: {pakuri_sel}\nAttack: {result[0]}\nDefense: {result[1]}\nSpeed: {result[2]}"
                    )
                except AssertionError as ae:
                    print("Error: No such Pakuri!")
                    # logging.debug(ae)
                # except IndexError as ie:
                #     logging.debug(ie)

            if action == 3:  # ADD PAKURI
                try:
                    assert (
                        self.pakudex.get_size() < self.pakudex.get_capacity()
                    ), "Error: Pakudex is full!"
                    pakuri_sel = input("Enter the name of the species to add: ")
                    assert (
                        self.pakudex.add_pakuri(pakuri_sel) == True
                    ), "Error in adding Pakuri"
                    print(f"Pakuri species {pakuri_sel} successfully added!")
                except AssertionError as ae:
                    print(ae)
                except Exception as e:
                    print("Unknown Error: ", e)

            if action == 4:  # EVOLVE PAKURI
                try:
                    pakuri_sel = input("Enter the name of the species to evolve: ")
                    assert isinstance(
                        self.pakudex.evolve_species(pakuri_sel), bool
                    ), "Error: No such Pakuri!"
                    print(f"{pakuri_sel} has evolved!")
                except AssertionError as ae:
                    print(ae)

            if (
                action == 5
            ):  # SORT PAKURI ::MAY HAVE TO MODIFY IF EXCEPTION FOR EMPTY PAKURI LIST::
                try:
                    assert self.pakudex.sort_pakuri() == True, "Error in sorting Pakuri"
                    print("Pakuri have been sorted!")
                except AssertionError as ae:
                    print(ae)

            if action == 6:  # EXIT
                print("Thanks for using Pakudex! Bye!")
                break  # only way to exit input menu loop


def main():
    program = Program()
    program.run()


if __name__ == "__main__":
    main()
