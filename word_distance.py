import re

class WordDistance:

  def __init__(self, text):
    self.words = re.compile('\w+').findall(text)

  def find_shortest_distance(self, start, end):
      return 0

