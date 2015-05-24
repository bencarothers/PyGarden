import PyGarden
import unittest
import re

class OptionsInput(unittest.TestCase):
    waterOptions = re.compile(r"#waterMe \d+|#waterMe")

    goodInput = "I am searching for #waterMe"
    goodInputWithTime = "I am searching for #waterMe 2"
    badInput = "Nothing here"
    faultyTime = "#waterMe -2"

    def testGoodInput(self):
        result = waterOptions.search(goodInput)
        self.assertEqual(result.group(),'#waterMe')

    def testFoodInputWithTime(self):
        result = waterOptions.search(goodInputWithTime)
        self.assertEqual(result.group(),'#waterMe 2')

    def testBadInput(self):
        result = waterOptions.search(badInput)
        self.assertEqual(result.group(),'')

    def testFaultyTime(self):
        result = waterOptions.search(faultyTime)
        self.assertEqual(result.group(),'#waterMe -2')

if __name__ == '__main__':
      unittest.main()
