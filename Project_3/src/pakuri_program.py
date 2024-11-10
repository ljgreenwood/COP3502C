from pakudex import Pakudex
import logging

logging.basicConfig(level=logging.DEBUG)

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

    def get_int_input(self, msg: str, err_msg: str = "Error") -> int:
        """
        sanity check input fetching function. prints the given error message for invalid inputs as specified
        I love typed function parameters!
        """
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
        # Prompt for / read pakudex capacity -> must return int so use get_int_input()
        self.pakudex.capacity = self.get_int_input(
            msg="Enter max capacity of the Pakudex: ",
            err_msg="Please enter a valid size.",
        )
        print(
            f"The Pakudex can hold {self.pakudex.capacity} species of Pakuri."
        )  # Print statement to show capacity of Pakudex
        # Display menu
        while True:
            self.menu()
            # Input action (selection) -> again must return int so use get_int_input()
            action = self.get_int_input(
                msg="What would you like to do? ",
                err_msg="Unrecognized menu selection!",
            )
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
                    assert result != None, "No Pakuri Found"
                    print(
                        f"Species: {pakuri_sel[0]}\nAttack: {pakuri_sel[1]}\nDefense: {pakuri_sel[2]}\nSpeed: {pakuri_sel[3]}"
                    )
                except AssertionError as ae:
                    print("Error: No such Pakuri!")
                    logging.debug(ae)
                except IndexError as ie:
                    logging.debug(ie)

            if action == 3:  # ADD PAKURI
                try:
                    pakuri_sel = input("Enter the name of the species to add: ")
                    assert self.pakudex.add_pakuri(pakuri_sel) != False
                    print(f"Pakuri species {pakuri_sel} successfully added!")
                except AssertionError:
                    print("No Pakuri in Pakudex yet!")
                except Exception as e:
                    print("Unknown Error: ", e)

            if action == 4:  # EVOLVE PAKURI
                pass

            if action == 5:  # SORT PAKURI
                pass

            if action == 6:  # EXIT
                break  # only way to exit input menu loop


def main():
    program = Program()
    program.run()


if __name__ == "__main__":
    main()
