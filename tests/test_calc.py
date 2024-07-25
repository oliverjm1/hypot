import pytest
from hypot.source import sqrt, hypot

# test sqrt function for even integer
def test_sqrt():
    input = 4
    e_output = 2.0
    assert sqrt(input) == e_output
    