"""Test cases for 7-eleven"""

#Standard library

#3rd Party library
import pytest

#project library
from seven_eleven.seven import print_7_eleven

#---------------------------------------------------------------------------
@pytest.mark.parametrize(
        "number, expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, "Seven"),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, "Eleven"),
            (14, "Seven"),
            (21, "Seven"),
            (22, "Eleven"),
            (76, 76),
            (77, "7-Eleven"),
            (154, "7-Eleven")
        ]
)
def test_print_7_eleven(number, expected):
    """Print 7-eleven."""
    result = print_7_eleven(number)
    assert result == expected
