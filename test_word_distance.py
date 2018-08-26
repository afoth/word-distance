import unittest
from word_distance import WordDistance 

class TestWordDistance(unittest.TestCase):

    def test_find_shortest_distance(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        distance = WordDistance(text).find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, 2)

    def test_find_shortest_distance_reversed(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        distance = WordDistance(text).find_shortest_distance('development', 'motivation')
        self.assertEqual(distance, 2)

    def test_find_shortest_distance_caseInsensitive(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        distance = WordDistance(text).find_shortest_distance('Motivation', 'Development')
        self.assertEqual(distance, 2)

    def test_find_shortest_distance_neighbors(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        distance = WordDistance(text).find_shortest_distance('We', 'do')
        self.assertEqual(distance, 0)

    def test_find_shortest_distance_startEqualsEnd(self):
        text = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        distance = WordDistance(text).find_shortest_distance('motivation', 'motivation')
        self.assertEqual(distance, -1)

    def test_find_shortest_distance_emptyList(self):
        distance = WordDistance('').find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, -1)

    def test_find_shortest_distance_listWithOneElement(self):
        distance = WordDistance('motivation').find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, -1)

    def test_find_shortest_distance_startNotInList(self):
        distance = WordDistance('We do development').find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, -1)

    def test_find_shortest_distance_endNotInList(self):
        distance = WordDistance('reward motivation in our team').find_shortest_distance('motivation', 'development')
        self.assertEqual(distance, -1)

if __name__ == '__main__':
    unittest.main()