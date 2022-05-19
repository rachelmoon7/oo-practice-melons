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
        if type(pairing) == str:
            self.pairings.append(pairing)
        elif type(pairing) == list:
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
  
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'green', False, False, 'Casaba')
    casaba.add_pairing(['strawberries', 'mint'])

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('prosciutto')
    
    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    # print("*********", all_melon_types)
    return all_melon_types
    

print(make_melon_types())

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")

# print(print_pairing_info(make_melon_types()))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    # print("-------------------------------", melon_types)
    code_dict = {}
    alltypes = make_melon_types()
    for inst in alltypes:
        code_dict[str(inst.code)] = inst

    return code_dict

print("****", make_melon_type_lookup(make_melon_types()))


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, type, shape_rating, color_rating, field, harvested_by):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_by_code = make_melon_type_lookup(melon_types)
    print("LINE 113", melon_by_code)
    melons = []

    melon1 = Melon(melon_by_code['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_by_code['yw'], 3, 4, 2, 'Sheila') 
    melon3 = Melon(melon_by_code['yw'], 9, 8, 3, 'Sheila') 
    melon4 = Melon(melon_by_code['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_by_code['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_by_code['cren'], 2, 3, 35, 'Michael')
    melon7 = Melon(melon_by_code['cren'], 2, 3, 4, 'Michael') 
    melon8 = Melon(melon_by_code['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_by_code['yw'], 7, 10, 3, 'Sheila')

    melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    return melons
print(make_melons(make_melon_types))

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    ourmels = make_melons(make_melon_types())

    for melon in ourmels:
        status = "(can be sold))"
        
        person = melon.harvested_by
        fieldnum = str(melon.field)

        if melon.is_sellable() == True:
            status = "(CAN BE SOLD)"
        else:
            status = "(NOT SELLABLE)"
        print(f"Harvested by {person} from Field {fieldnum} {status}")

        #Harvested by Sheila from Field 2 (CAN BE SOLD)
print(get_sellability_report(make_melons(make_melon_types())))
