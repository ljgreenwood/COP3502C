from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20):
        """
        initializes the capacity (default value 20) and the list of pakuri (pocket)
        """
        self.capacity = capacity  # total capacity of pakudex
        self.pocket = []  # list of pakuri (len(**) = size)

    def get_size(self):
        """
        returns the length of the pocket list
        """
        return len(self.pocket)

    def get_capacity(self) -> int:
        """
        returns the self.capacity value given in initialization
        """
        return self.capacity

    def add_pakuri(self, species) -> bool:
        """
        attempt to add pakuri to the list (in order of adding -- not sorted), returns success/failure bool
        """
        try:
            self.pocket.append(
                Pakuri(species)
            )  # will exit the try when an error is raised
            return True
        except:
            return False  # unsuccessful in adding the Pakuri to the pocket

    def get_species_array(self):
        """
        returns none if there is not species in the array, else returns the list
        """
        try:  # attempt at getting list
            temp = [pakuri_inst.get_species() for pakuri_inst in self.pocket]
            # access the keys of the pakuri pocket dict and cast to a list
            assert len(temp) != 0  # assert a non-empty list of keys
            return temp
        except AssertionError:  # list is empty
            return None  # this will tell the main program that there were no pakuri in the dict

    def get_stats(self, species):
        try:
            for (
                pakuri_obj
            ) in (
                self.pocket
            ):  # object of species (will exit if KeyError) (species isn't found)
                if pakuri_obj.get_species() == species:
                    return [
                        pakuri_obj.get_attack(),
                        pakuri_obj.get_defense(),
                        pakuri_obj.get_speed(),
                    ]  # [attack, defense, speed]
        except:
            return None

    def evolve_species(self, species):
        try:
            for (
                pakuri_obj
            ) in (
                self.pocket
            ):  # pakuri object of species (will exit if KeyError - species not found)
                if pakuri_obj.get_species() == species:
                    pakuri_obj.evolve()  # call pakuri evolve method
                    return True
        except:
            return False

    def sort_pakuri(self):
        try:
            self.pocket.sort(key=lambda pakuri_obj: pakuri_obj.get_species())
            return True
        except:
            return False


# paku = Pakudex()
# paku.add_pakuri('wefwkfajsdlfjaslkd')
# paku.add_pakuri('pijaku')
# print(paku.get_species_array())
# paku.sort_pakuri()
# print(paku.get_species_array())
