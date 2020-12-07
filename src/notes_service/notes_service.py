from src.notes_storage.notes_storage import NotesStorage


class NotesService:
    def __init__(self):
        self.notes_storage = NotesStorage()

    def add(self, note):
        self.notes_storage.add(note)

    def average_of(self, name):
        result = self.notes_storage.get_all_notes_of(name)
        wynik = 0
        if not result:
            return 'Name does not exist'
        for note in result:
            wynik += note.get_note()
        return wynik/len(result)

    def clear(self):
        self.notes_storage.clear()