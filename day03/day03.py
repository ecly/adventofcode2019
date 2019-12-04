from collections import defaultdict


def plot_wire(wire):
    wire_map = defaultdict(int)
    x, y = 0, 0
    steps = 0
    delta_map = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for m in wire.split(","):
        direction = m[0]
        dx, dy = delta_map[direction]
        amount = int(m[1:])
        for _ in range(amount):
            steps += 1
            x += dx
            y += dy
            wire_map[x, y] += steps

    return wire_map


def get_intersection_map(map1, map2):
    intersection_map = defaultdict(int)
    intersections = set(map1.keys()).intersection(map2.keys())
    for pos in intersections:
        wire1_steps = map1[pos]
        wire2_steps = map2[pos]
        intersection_map[pos] = map1[pos] + map2[pos]

    return intersection_map


def main():
    wire1 = input()
    wire2 = input()

    map1 = plot_wire(wire1)
    map2 = plot_wire(wire2)
    wire_map = get_intersection_map(map1, map2)
    intersections = wire_map.keys()
    distances = [abs(x) + abs(y) for x, y in intersections]
    print(min(distances))

    min_combined_steps = min(wire_map.values())
    print(min_combined_steps)


if __name__ == "__main__":
    main()
