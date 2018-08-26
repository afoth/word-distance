import re

class WordDistance:

  def __init__(self, text):
    # extract words from given text
    self.words = re.compile('\w+').findall(text.lower())

  # finds shortest distance in number of words between start and end
  # returns -1 if start in the list and start equals end
  # returns -1 if start or end not in the list
  def find_shortest_distance(self, start, end):
    start = start.lower()
    end = end.lower()
    min_dist = -1
    last = -1
    # pre-checks
    if start == end or len(self.words) < 2:
      return -1
    # iterate over the list of words
    # calculate distance of last occurrence with the current element if matching start or end
    for i in range(len(self.words)):
        if self.words[i] == start or self.words[i] == end:
          dist = i - last - 1
          if self.words[i] != self.words[last] and last >= 0 and (dist < min_dist or min_dist < 0):
            min_dist = dist
          last = i
    return min_dist


