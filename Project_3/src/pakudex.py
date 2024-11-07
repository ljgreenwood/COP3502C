from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity  # total capacity of pakudex
        self.pocket = {}  # list of pakuri (len(**) = size)

    def get_size(self):
        return len(self.pocket)

    def get_capacity(self):
        return self.capacity

    def add_pakuri(self, species):
        try:
            self.pocket[species] = Pakuri(
                species
            )  # will exit the try when an error is raised
            return True
        except:
            return False  # unsuccessful in adding the Pakuri to the pocket

    def get_species_array(self):
        try:  # attempt at getting list
            temp = list(
                self.pocket.keys()
            )  # access the keys of the pakuri pocket dict and cast to a list
            assert len(temp) != 0  # assert a non-empty list of keys
            return temp
        except AssertionError:  # list is empty
            return None  # this will tell the main program that there were no pakuri in the dict

    def get_stats(self, species):
        try:
            pakuri_obj = self.pocket[
                species
            ]  # object of species (will exit if KeyError) (species isn't found)
            return [
                pakuri_obj.get_attack(),
                pakuri_obj.get_defense(),
                pakuri_obj.get_speed(),
            ]  # [attack, defense, speed]
        except:
            return None

    def evolve_species(self, species):
        try:
            pakuri_obj = self.pocket[
                species
            ]  # pakuri object of species (will exit if KeyError - species not found)
            pakuri_obj.evolve()  # call pakuri evolve method
            return True
        except:
            return False

        # list of strings containing species as ordered in pakudex, return none if no species have been added

    def sort_pakuri(self):
        list(self.pocket.items()).sort()


pakudex = Pakudex()
print(pakudex.pocket)
print(pakudex.get_species_array())
print(pakudex.add_pakuri("pikaju"))
print(pakudex.add_pakuri("tryranasoar"))
print(pakudex.pocket)
print(pakudex.get_species_array())
print(pakudex.get_stats("pikaju"))
print(pakudex.evolve_species("pikaju"))
print(pakudex.get_stats("pikaju"))
print(pakudex.sort_pakuri())
