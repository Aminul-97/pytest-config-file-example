import pytest
from src.distance_calculator import (
    kilometer_to_mile,
    mile_to_kilometer
)


def test_distance_calculator():
    assert kilometer_to_mile(5) == 3.106855
    assert mile_to_kilometer(3.106855) == 5
