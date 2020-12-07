import unittest
from src.note.note import Note


class TestNote(unittest.TestCase):
    def test_note_setting(self):
        Note('abc', 3.5)

    def test_note_type_error1(self):
        name = 123
        note = 4.0
        self.assertRaises(TypeError, Note, name, note)

    def test_note_type_error2(self):
        name = None
        note = 4.0
        self.assertRaises(TypeError, Note, name, note)

    def test_note_type_error3(self):
        name = 'Name'
        note = 'note'
        self.assertRaises(TypeError, Note, name, note)

    def test_note_value_error1(self):
        name = ''
        note = 3
        self.assertRaises(ValueError, Note, name, note)

    def test_note_value_error2(self):
        name = 'Abc'
        note = 0.3
        self.assertRaises(ValueError, Note, name, note)

    def test_note_get_name(self):
        name = 'Abc'
        note = 3.5
        test_object = Note(name, note)
        self.assertEqual(test_object.get_name(), name)

    def test_note_get_note(self):
        name = 'Abc'
        note = 3.5
        test_object = Note(name, note)
        self.assertEqual(test_object.get_note(), note)
