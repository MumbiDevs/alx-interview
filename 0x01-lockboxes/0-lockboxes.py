def canUnlockAll(boxes):
    # Create a set to keep track of unlocked boxes
    unlocked = {0}  # Start with the first box
    keys = [0]  # Start with the key for the first box

    while keys:
        current_key = keys.pop()  # Get the last key to process
        for key in boxes[current_key]:  # Check the keys in the current box
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)  # Unlock the box if it hasn't been unlocked
                keys.append(key)  # Add the new key to the keys to process

    # Check if we managed to unlock all boxes
    return len(unlocked) == len(boxes)

# Example usage
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
