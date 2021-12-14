import unittest
from parameterized import parameterized
from modules.Note import Note

class Test_Note(unittest.TestCase):
    def test_positive_get_name(self):
      note = Note("name", 3)
      self.assertEqual(note.get_name(), "name")
    def test_positive_get_note(self):
      note = Note("name", 3)
      self.assertEqual(note.get_note(), 3)
    @parameterized.expand([
      ("name", 2.22),
      ("name", 3.333),
      ("name", 4.4444),
      ("name", 5.55555),
      ("name", 6.000000)
    ])
    def test_positine_note_float(self, name, note):
      Note(name, note)
      self.assertTrue(True)
    @parameterized.expand([
      (" ", 3),
      ("!@#$%^&*()", 3),
      ("name", 3),
      ("(. y .)", 3)
    ])
    def test_positine_name_float(self, name, note):
      Note(name, note)
      self.assertTrue(True)
      # name exceptions
    def test_exception_name_none(self):
      self.assertRaises(Exception, Note, None, 3)
    def test_exception_name_empty(self):
      self.assertRaises(Exception, Note, "", 3)
    @parameterized.expand([
      ([], 3),
      (["name"], 3),
      ({"name": "note"}, 3),
      (3, 3),
      (3.333, 3)
    ])
    def test_exception_name_wrong_type(self, bad_name, note):
      self.assertRaises(Exception, Note, bad_name, note)
      # note exceptions
    @parameterized.expand([
      ("name", -23456),
      ("name", 0),
      ("name", 1.9999999)
    ])
    def test_exception_note_under_2(self, name, bad_note):
      self.assertRaises(Exception, Note, name, bad_note)
    @parameterized.expand([
      ("name", 23456),
      ("name", 10),
      ("name", 6.00000001)
    ])
    def test_exception_note_over_6(self, name, bad_note):
      self.assertRaises(Exception, Note, name, bad_note)
    @parameterized.expand([
      ("name", ""),
      ("name", "3"),
      ("name", []),
      ("name", [3]),
      ("name", {"3": 3})
    ])
    def test_exception_note_wrong_type(self, name, bad_note):
      self.assertRaises(Exception, Note, name, bad_note)

if __name__ == "__main__":
    unittest.main()