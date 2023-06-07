import unittest

class forTest(unittest.TestCase):
    def test_1(self):
        inp = "TEST".lower()
        out = 'test'
        self.assertEqual(inp, out)
        
    def test_2(self):
        inp = "TEST".lower()
        self.assertTrue(inp.isupper(), "not upper")
        
# unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(forTest)
unittest.TextTestRunner().run(suite)