def bestCoordinate(towers: [[int]], radius: int) -> [int]:
    import math
    max_power = 0
    max_power_pos = [0, 0]
    for i in range(51):
        for j in range(51):
            temp_power = 0
            for tower in towers:
                dist = math.sqrt(abs(tower[0] - i) ** 2 + abs(tower[1] - j) ** 2)
                if dist <= radius:
                    temp_power += math.floor(tower[2] / (1 + math.sqrt(abs(tower[0] - i) ** 2 + abs(tower[1] - j) ** 2)))
            if temp_power > max_power:
                max_power = temp_power
                max_power_pos = [i, j]
    return max_power_pos

tower = [[50,20,31],[43,36,29]]
radius = 38

print(bestCoordinate(tower, radius))