DATA = {'Grandma': 100, 'Factory': 500, 'Mine': 2000, 'Shipment': 7000,
        'Alchemy': 50000, 'Portal': 1000000, 'Time_Machine': 123645798}

ID = {'Grandma': 'buyGrandma', 'Factory': 'buyFactory', 'Mine': 'buyMine', 'Shipment': 'buyShipment',
      'Alchemy': 'buyAlchemy lab', 'Portal': 'buyPortal', 'Time_Machine': 'buyTime machine'}


class Check:
    def __init__(self):
        self.invest = None
        self.id = None

    def value_check(self, saved=50000):
        for _ in DATA:
            if saved <= DATA[_]:
                self.invest = _
                self.id = ID[_]
                break
            else:
                continue
