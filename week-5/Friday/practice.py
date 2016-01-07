class Mymagic:
    def __init__(self, list_of_users):
        self.database = list_of_users

    def name_lists(self):
        return list(map(lambda names : names['name'], self.database))

    def name_lists_j(self):
        return list(filter(lambda names : names.startswith('J'), self.name_lists()))
