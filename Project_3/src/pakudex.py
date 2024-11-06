from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity  # total capacity of pakudex
        self.pocket = {} # list of pakuri (len("") = size)

    def get_size(self):
        return len(pakuri)

    def get_capacity(self):
        return self.capacity 

    def add_pakuri(self, species):
        try:
            self.pocket[species] = Pakuri(species)
            # will exit the try when an error is raised
            return True
        except:
            return False

    def get_species_array(self):
        try:  # getting list
            temp = list(self.pocket.keys())
            assert len(temp) != 0 
            return temp
        except AssertionError:  # list is empty
            return None

    def get_stats(self, species):
        pass

    def evolve_species(self, species):
        pass

        # list of strings containing species as ordered in pakudex, return none if no species have been added

    def get_stats(self, species):
        try:
            pass
        except:
            return None

pakudex = Pakudex()

print(pakudex.pocket)
print(pakudex.get_species_array())
print(pakudex.add_pakuri("pikaju"))
print(pakudex.add_pakuri("tryranasoar"))
print(pakudex.pocket)
print(pakudex.get_species_array())
print(pakudex.get_stats("pikaju"))

        
