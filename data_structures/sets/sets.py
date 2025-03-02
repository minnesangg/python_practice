friends_A = ["Alice", "Bob", "Charlie", "David"]
friends_B = ["Charlie", "Emma", "Alice", "Frank"]

def common_friends(*, first = friends_A, second = friends_B) -> list:
    intersections = set(first).intersection(set(second))
    return list(intersections)

def different_friends(*, first = friends_A, second = friends_B) -> list:
    differences = set(first).difference(set(second))
    return list(differences)

def exclusive_friends(*, first = friends_A, second = friends_B) -> list:
    exclusive1 = different_friends(first = first, second = second)
    exclusive2 = different_friends(first = second, second = first)

    return exclusive1 + exclusive2



print(common_friends(first = friends_A, second = friends_B))
print(different_friends(first = friends_A, second = friends_B))
print(exclusive_friends(first = friends_A, second = friends_B))
