"""

Complete the update_party_health function.

It receives two lists of equal length:

- health_points contains each party member's current health

- damage_taken contains the damage each matching party member takes

- Return a new list containing each party member's remaining health in the same order. Health cannot fall below 0.

Do not change either input list.

For example:

health = [50, 30, 80]
damage = [10, 35, 20]

print(update_party_health(health, damage))
# [40, 0, 60]

"""

def update_party_health(health_points, damage_taken):
    remaining_health = []
    
    for point in range(len(health_points)):
        if health_points[point] < damage_taken[point]:
            remaining_health.append(0)
        else:
            result = health_points[point] - damage_taken[point]
            remaining_health.append(result)
    return remaining_health