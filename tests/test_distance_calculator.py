from src.distance_calculator import kilometer_to_mile, mile_to_kilometer


def test_kilometer_to_mile():
    assert kilometer_to_mile(5) == 3.106855

def test_mile_to_kilometer():
    assert mile_to_kilometer(3.106855) == 5