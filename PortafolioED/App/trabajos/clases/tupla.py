class Tupla:
    def __init__(self):
        self.tuple_list = []

    def save_tuple(self, data):
        self.tuple_list.append(data)
        return data