# Word Distance Calculator

A simple python programm for word distance calculation.
Given any two words, it finds the shortest distance between them in terms of numbers of words in between.

Program reads text files and iterates over the words in the file trying to find start and end words.
When found it calculates and displays the absolute distance between them (number of words).

E.g. for _We do value and reward motivation in our development team. Development is a key skill for a DevOp._ and _we_ as start and _value_ as end _1_ is calculated as distance.
If start or/and end is not present in the file, the result will be _-1_. Same if the start and the end are equal. The case and the order of words are ignored.


## Requirements

Python 3.6 or newer

No further dependencies


## Usage

In order to calculate distance between words run `python word_distance.py INPUT_FILE START_WORD END_WORD`

e.g. `python word_distance.py sample.txt motivation development`


## How to run tests

Tests are written using _unittest_ as testing framework

Run `python -m unittest test_word_distance`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details