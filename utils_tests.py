import utils
import unittest

class Test(unittest.TestCase):
    def test(self):
        test = utils.utils()
        print("===")
        print("Test reverse")
        self.assertEqual(test.reversed("hello"), None)
        self.assertEqual(test.reversed(1.0), None)
        self.assertEqual(test.reversed(12345), 54321)

        print("===")
        print("Test formatter")
        self.assertEqual(test.formatter("hello"),None)
        self.assertEqual(test.formatter(1.0),None)
        self.assertEqual(test.formatter(9), ("1001","11"))
        
        print("===")
        print("All tests pass")

def main():
    my_tests = Test()
    my_tests.test()

if __name__=="__main__":
    main()