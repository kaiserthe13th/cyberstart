points = [(1, 2), (3, 4), (1, 8), (2, 6)]
distances = []

def euclidian_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2+(y2 - y1)**2)**0.5

for point1 in points:
    for point2 in points:
        if point1 == point2:
            continue
        distances.append(euclidian_distance(point1, point2))

min_distance = min(distances)

print(min_distance)
