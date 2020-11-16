import pytest
from Let_it_Burn import smoke
from Let_it_Burn import house

from Let_it_Burn import createCoordinates

# @pytest.fixture()
# def setup():
#
#     createCoordinates(house)



# Find way to reset house variable as currently a global variable that can easily go wrong.
# Alternatively have a house setup exclusively for testing?
# Find way to reset house variable before each test (fixtures didn't work) or just follow along
# example as fallback.
def test_CanApplySmokeToEmptySpaces():
    assert house[1][9] == "S"

def test_SingleSpaceCatchesFireIfSmokeAppliedToSmoke():
    assert house[5][5] == "F"

# Only really tests going down tiles.
def test_FireSpreadsAcrossSmoke():
    assert house[1][1] and house[2][1] and house[3][1] == "F"



# Only really tests the checking to the left, also doesn't test through open doors.
def test_FireSpreadsToSmokeThroughWalls():
    assert house[5][7] == "F"


def test_smokeCatchesFireWhenPlacedNextToFire():
    assert house[2][2] == "F"
