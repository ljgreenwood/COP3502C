import sys
from cow import Cow
import heifer_generator  # heifer_generator.get_cows()

def list_cows(cows):
    cow_string = 'Cows available: '
    for cow in cows:
        cow_string += cow.name + " "
    print(cow_string[:-1])

def find_cow(name, cows):
    for cow in cows:
        if name == cow.name:
            return cow
    return None

def main():
    args = sys.argv[1:]
    all_cows = heifer_generator.get_cows()
    if args[0] == '-l':
        list_cows(all_cows) 
    else: 
        if args[0] == '-n':
            args.pop(0)  # remove the -n argument from the list
            name = args.pop(0)  # take the name argument from the list
        else:
            name = 'heifer'

        cow_found = find_cow(name, all_cows)
        message = " ".join(args) 
        
        if cow_found:
            print(message)
            print(cow_found.image)
        else:
            print(f"Could not find {name} cow!")


if __name__ == '__main__':
    main()

