def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    stack = [(0, 0)]  # Start with both jugs empty
    visited = set()

    while stack:
        current_state = stack.pop()
        jug1, jug2 = current_state

        if current_state in visited:
            continue

        visited.add(current_state)

        if jug1 == target or jug2 == target:
            print("Solution found:", current_state)
            return

        # Fill jug1
        stack.append((capacity_jug1, jug2))

        # Fill jug2
        stack.append((jug1, capacity_jug2))

        # Empty jug1
        stack.append((0, jug2))

        # Empty jug2
        stack.append((jug1, 0))

        # Pour from jug1 to jug2
        pour = min(jug1, capacity_jug2 - jug2)
        stack.append((jug1 - pour, jug2 + pour))

        # Pour from jug2 to jug1
        pour = min(jug2, capacity_jug1 - jug1)
        stack.append((jug1 + pour, jug2 - pour))

    print("Solution not found.")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_water = 2

    water_jug_dfs(jug1_capacity, jug2_capacity, target_water)
