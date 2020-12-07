from unittest.mock import *
import unittest
from src.notes_service.notes_service import NotesService
from src.notes_storage.notes_storage import NotesStorage
from src.note.note import Note


class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_add_note(self, mock_method):
        name = 'Olek'
        note = 3.5
        mock_method.return_value = [Note('Olek', 3.5)]
        self.temp.add(Note(name, note))
        self.assertEqual(self.temp.average_of(name), 3.5)

    @patch.object(NotesStorage, 'add')
    def test_add_note_exception(self, mock_method):
        mock_method.side_effect = TypeError('error')
        self.assertRaises(TypeError, self.temp.add, 'note')

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_average(self, mock_method):
        self.temp.add(Note('Olek', 2.0))
        self.temp.add(Note('Olek', 4.0))
        mock_method.return_value = [Note('Olek', 2.0), Note('Olek', 4.0)]
        self.assertEqual(self.temp.average_of('Olek'), 3.0)

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_average_name_does_not_exist(self, mock_method):
        self.temp.add(Note('Olek', 2.0))
        mock_method.return_value = []
        self.assertEqual(self.temp.average_of('Maciej'), 'Name does not exist')

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_average_exception(self, mock_method):
        mock_method.side_effect = TypeError('error')
        self.assertRaises(TypeError, self.temp.average_of, 123)

    def test_clear(self):
        self.temp.add(Note('Olek', 2.0))
        self.temp.add(Note('Olek', 2.0))
        self.temp.notes_storage.notes = []
        self.temp.clear()
        self.assertEqual(self.temp.notes_storage.notes, [])