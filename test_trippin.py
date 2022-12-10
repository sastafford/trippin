from trippin import format_name
import unittest

class TestHelpers(unittest.TestCase):

    def test_format_name(self):
        assert(format_name("washington d.c.") == "WASHINGTON D.C.")
