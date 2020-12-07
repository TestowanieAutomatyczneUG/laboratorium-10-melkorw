class Note:
    def __init__(self, name, note):
        if type(name) is not str or name is None or (type(note) is not float
                                                     and type(
                    note) is not int):
            raise TypeError('Bad types')

        if name == '' or note < 2 or note > 6:
            raise ValueError('Bad values')

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
