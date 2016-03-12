import unittest

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "\n\t\t-- Preparing tests. --\n"

    def test_first(self):
        self.assertEqual(int('4')-1,4-1)
        self.assertFalse(False)
        self.assertTrue("aren't you cute?" != "yes you are!")
        with self.assertRaises(Exception):
            raise Exception

    def test_skip_it(self):
        raise unittest.SkipTest

    def test_at_coffee_break(self):
        self.assertLess('coffee', 'tea')

    @classmethod
    def tearDownClass(self):
        print "\n\n\t-- Everything was alright! See ya! --\n"

if __name__ == '__main__':
    unittest.main()
