from pprint import pprint


def preparemaps():  # run this to generate two text file, map1.txt and map2.txt
    m1 = [
        "WWWWWWWWWWWWWWWWWW.WWWWWWW",
        "WWWWWWWW.WWWWWWWW...WWWWWW",
        "WWWWW...WWWWWWWWWW.B..WWWW",
        "WWWWWWW.WWWWWWWWW...WWWWWW",
        "WWWWWWW.....WWWWWWWW..WWWW",
        "WWW.......WWWWWWWWWWWWWWWW",
        "WWWW...A..WWWWWWWWWWW..WWW",
        "WWWWW.....WWWWWWWW...WWWWW",
        "WWWWWWW..WWWWWWWWW.C.WWWWW",
        "WWWW..WWWWWWWWWWWW...WWWWW",
        "WW....WWWWWWWWWWWWWWWWWWWW",
        "WWW.WWWWWWWWWWWWWWWWWWWWWW",
    ]
    map1file = open("map1.txt", "w")
    for r in m1:
        map1file.write(r + "\n")
    m2 = [
        "WWWWWWWWWWWWWWW.WWWWWWW",
        "WWWWW.WWWWWWWW...WWWWWW",
        "WWWWWWWWWWWWWWW.B..WWWW",
        "WWWW.WW.WWWWWW...WWWWWW",
        "WWWW...WWWWWWWWWW..WWWW",
        "W......WWWWWWWWWWWWWWWW",
        "W...A..WWWWWWWWWWW..WWW",
        "WW.....WWWWWWWW...WWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWW",
    ]
    map2file = open("map2.txt", "w")
    for r in m2:
        map2file.write(r + "\n")


# This will read in a file and covert it into a 2D array
# You do not need to use it if you have another way to solve Part 2
# However, if you use this code, please remember to include in your submission
def readmap(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(list(line.rstrip("\n")))
    return m


def crop_map(filename, minr, maxr, minc, maxc):
    map = readmap(filename)
    cropped_map = []
    # limit maxr and maxc to the size of the map
    minr = max(minr, 0)
    minc = max(minc, 0)
    maxr = min(maxr, len(map))
    maxc = min(maxc, len(map[0]))
    for i in range(minr, maxr):
        cropped_map.append("".join(map[i][minc:maxc]))
    return cropped_map


# pprint(crop_map("map1.txt", 5, 9, 3, 25))
# pprint(crop_map("map1.txt", 7, 10, -10, 40))
# pprint(crop_map("map1.txt", 3, 3, 4, 4))
# pprint(crop_map("map0.txt", 5, 9, 2, 2))
# pprint(crop_map("map1.txt", -10, 100, 3, 4))


def island_area(filename, prince):
    map = readmap(filename)
    # find the prince's location
    location = (None, None)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == prince:
                location = (i, j)
                break
        if location != (None, None):
            break
    if location == (None, None):
        raise ValueError("Prince not found in map")
    # flood fill to find the area of the island
    area = 0
    stack = [location]
    while stack:
        i, j = stack.pop()
        if i < 0 or i >= len(map) or j < 0 or j >= len(map[i]):
            continue
        if map[i][j] == "W":
            continue
        area += 1
        map[i][j] = "W"
        stack.append((i - 1, j))
        stack.append((i + 1, j))
        stack.append((i, j - 1))
        stack.append((i, j + 1))
    return area


print(island_area("map1.txt", "A"))
print(island_area("map1.txt", "B"))
print(island_area("map1.txt", "C"))
print(island_area("map2.txt", "A"))
