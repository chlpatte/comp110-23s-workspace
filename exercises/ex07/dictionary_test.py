"Test for the dictionary functions for ex07!"

__author__ = "730580489"

import pytest

from exercises.ex07.dictionary import invert

with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)