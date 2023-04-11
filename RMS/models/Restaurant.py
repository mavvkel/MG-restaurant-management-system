class Restaurant:
    def __init__(self, availability):
        self._availability = availability
        self._workers = []
        self._tables = []
        self._menu = []

    def get_availability(self):
        return self._availability

    def set_availability(self, availability):
        self._availability = availability

    def get_workers(self):
        return self._workers

    def add_or_update_worker(self, worker):
        if worker not in self._workers:
            self._workers.append(worker)

    def remove_worker(self, worker):
        if worker in self._workers:
            self._workers.remove(worker)

    def get_tables(self):
        return self._tables

    def add_or_update_table(self, table):
        if table not in self._tables:
            self._tables.append(table)

    def remove_table(self, table):
        if table in self._tables:
            self._tables.remove(table)

    def get_menu(self):
        return self._menu

    def add_or_update_menu_entry(self, menu_entry):
        if menu_entry not in self._menu:
            self._menu.append(menu_entry)

    def remove_menu(self, menu_entry):
        if menu_entry in self._menu:
            self._menu.remove(menu_entry)
