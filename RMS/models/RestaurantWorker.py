from RestaurantWorkerRole import RestaurantWorkerRole

class RestaurantWorker:
    def __init__(self, name, role, availability):
        self.name = name
        self.role = role
        self.availability = availability
        self.tables = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, table):
        if table in self.tables:
            self.tables.remove(table)

    def get_tables(self):
        return self.tables
