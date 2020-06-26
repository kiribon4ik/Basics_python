class Warehouse:
    def __init__(self):
        self.equip_list = []
        self.num_places = 50


class OfficeEquipment:
    def __init__(self, name, quantity, brand_new=False):
        self.name = name
        self.quantity = quantity
        self.brand_new = brand_new


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, print_speed, brand_new=False):
        super().__init__(name, quantity, brand_new)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, scan_speed, brand_new=False):
        super().__init__(name, quantity, brand_new)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, num_copies, brand_new=False):
        super().__init__(name, quantity, brand_new)
        self.num_copies = num_copies
