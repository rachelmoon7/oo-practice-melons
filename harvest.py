############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name, pairings = " "
    ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []
    

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)
        print(f"Pairs well with {pairing}")


# yellowMellon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
# print(yellowMellon.add_pairing('ice cream'))
# print(yellowMellon.pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
           


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

  
    Muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    Casaba = MelonType('cas', 2003, 'green', False, False, 'Casaba')
    Crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    Yellow_Watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')

    our_melons = [Muskmelon, Casaba, Crenshaw, Yellow_Watermelon]

    for melon in our_melons:
        all_melon_types.append(melon.name)

    print(all_melon_types)
print(make_melon_types())

   # for melons in different_melons:
   #     melon.add_pairing(pairing)

    # return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
