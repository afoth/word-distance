import re

class WordDistance:

  def __init__(self, text):
    # extract words from given text
    self.words = re.compile('\w+').findall(text)

  # finds shortest distance in number of words between start and end
  def find_shortest_distance(self, start, end):
    min_dist = -1
    i = 0
    last = 0
    for i in range(len(self.words)):
        if self.words[i] == start or self.words[i] == end:
            dist = i - last - 1
            if self.words[last] != self.words[i] and (dist < min_dist or min_dist < 0):
                min_dist = dist
            last = i
    return min_dist

