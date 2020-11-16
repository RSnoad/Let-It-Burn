from time import sleep


# Global variable causing issues.
house = ["#############/#",
         "#     |       #",
         "#     #       #",
         "#     #       #",
         "#######       #",
         "#     _       #",
         "###############"]

def createCoordinates(house):
    house = list(map(list, house))
    return house


house = createCoordinates(house)


def smoke(x, y):
    placeSmoke(x, y)
    fireSpreads(x, y)
    # print(x, y)
    displayHouse()



def placeSmoke(x, y):
    if house[y][x] == " ":
        house[y][x] = "S"
    elif house[y][x] == "S":
        house[y][x] = "F"


def fireSpreads(x, y):
    fireSpreadsToSmokeWhenSmokePlaced(x, y)
    fireSpreadsWhenFirePlaced(x, y)


def displayHouse():
    outhouse = [' '.join([str(i) for i in lst]) for lst in house]
    for row in outhouse:
        print(row)
    sleep(1)



# TODO Extract if statements/ meaningful variables from this as many repetitions.
def fireSpreadsWhenFirePlaced(x, y):
    # Ensure tile is on fire, is an open door or a damaged wall.
    if house[y][x] == "F" or house[y][x] == "/" or house[y][x] == "_":

        # Check tile above
        fireSpreadsToSingleTiles(x, y - 1)

        # Check tile below
        fireSpreadsToSingleTiles(x, y + 1)

        # Check tile to the left
        fireSpreadsToSingleTiles(x - 1, y)

        # Check tile to the right
        fireSpreadsToSingleTiles(x + 1, y)


def fireSpreadsToSingleTiles(x, y):
    # If tile is smoke then fire spreads to tile, then check surrounding tiles for smoke to spread further.
    if house[y][x] == "S":
        house[y][x] = "F"
        fireSpreadsWhenFirePlaced(x, y)
    # If tiles is an open door or damaged wall, then allow fire to spread to smoke on the other side.
    if house[y][x] == "/" or house[y][x] == "_":
        fireSpreadsWhenFirePlaced(x, y)

def fireSpreadsToSmokeWhenSmokePlaced(x, y):

    if house[y][x] == "S":
        up = house[y - 1][x]
        down = house[y + 1][x]
        right = house[y][x + 1]
        left = house[y][x - 1]

        # Check surrounding tiles for fire when smoke placed.
        if up == "F" or down == "F" or left == "F" or right == "F":
            house[y][x] = "F"
        # Check tile above for open doors or broken walls, and spread fire to smoke if fire on other side.
        if (up == "/" or up == "_") and house[y - 2][x] == "F":
            house[y][x] = "F"
        # Check below
        if (down == "/" or down == "_") and house[y + 2][x] == "F":
            house[y][x] = "F"
        # Check to the left
        if (left == "/" or left == "_") and house[y][x - 2] == "F":
            house[y][x] = "F"
        # Check to the right
        if (right == "/" or right == "_") and house[y][x + 2] == "F":
            house[y][x] = "F"


smoke(1,1)
smoke(1,2)
smoke(1,3)
smoke(5,6)
smoke(2,4)
smoke(1,1)
smoke(1,2)
smoke(5,5)
smoke(5,5)
smoke(9,1)
smoke(7,5)
smoke(2,2)
