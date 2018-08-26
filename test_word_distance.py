import unittest
from word_distance import WordDistance 

class TestWordDistance(unittest.TestCase):

    def setUp(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        self.wd = WordDistance(text)

    def test_find_shortest_distance(self):
        distance = self.wd.find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, 2)

if __name__ == '__main__':
    unittest.main()