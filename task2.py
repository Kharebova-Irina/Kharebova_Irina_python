
import sys
import math

def circle_data(file_path):
    with open(file_path, 'r') as file:
        x = float(file.readline().strip())
        y = float(file.readline().strip())
        radius = float(file.readline().strip())
    return (x, y, radius)

def points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def position_data(circle, point):
    x0, y0, radius = circle
    x1, y1 = point
    dist = (x1 - x0)**2 + (y1 - y0)**2
    radius_2 = radius**2

    if math.isclose(dist, radius_2, rel_tol=1e-20):
        return 0
    elif dist < radius_2:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Error")
        return

    cfile = sys.argv[1]
    pfile = sys.argv[2]

    circle = circle_data(cfile)
    points = points_data(pfile)

    for point in points:
        position = position_data(circle, point)
        print(position)

if __name__ == "__main__":
    main()
