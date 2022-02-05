from Main import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_is_field(self):
        self.assertEqual(is_field("asdasdsad.asdasd()"), False)
        self.assertEqual(is_field("ass.bruh"), True)

    def test_is_constructor(self):
        self.assertEqual(is_constructor("Bruh.Bruh()"), True)
        self.assertEqual(is_constructor("Bruh.Bruhh()"), False)
        self.assertEqual(is_constructor("Bruh.Bruh(boolean, IMotif)"), True)

    def test_str_to_method(self):
        self.assertEqual(process_str_to_method("ILoMotif.descList(boolean)"),
                         ("descList", "boolean"))
        self.assertEqual(process_str_to_method("ConsLoMotif.sumMotifs()"),
                         ("sumMotifs", ""))
        self.assertEqual(process_str_to_method("ConsLoMotif.sumMotifs(amongus, int, sus)"),
                         ("sumMotifs", "amongus, int, sus"))


if __name__ == '__main__':
    unittest.main()
