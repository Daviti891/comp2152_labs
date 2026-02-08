# Lab 04: Loops and Functions Practice
# Student Name: Daviti Sidana 


def robot_returns_to_origin(moves):
    x, y = 0, 0
    for move in moves:
        if move == 'U': y += 1
        elif move == 'D': y -= 1
        elif move == 'L': x -= 1
        elif move == 'R': x += 1
    return x == 0 and y == 0

def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

def two_sum_optimized(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        needed = target - num
        if needed in seen: return (seen[needed], i)
        seen[num] = i
    return None

def shuffle_array(nums, n):
    first, second = nums[:n], nums[n:]
    result = []
    for i in range(n):
        result.append(first[i])
        result.append(second[i])
    return result

def count_characters(s):
    counts = {}
    for char in s: counts[char] = counts.get(char, 0) + 1
    return counts

def first_unique_character(s):
    char_counts = count_characters(s)
    for i in range(len(s)):
        if char_counts[s[i]] == 1: return i
    return -1

# Test cases (Required for full marks)
print(f"Robot 'UD': {robot_returns_to_origin('UD')}")
print(f"Two Sum [2,7,11,15] (9): {two_sum_optimized([2,7,11,15], 9)}")
print(f"Shuffle [2,5,1,3,4,7]: {shuffle_array([2,5,1,3,4,7], 3)}")
print(f"Unique 'leetcode': {first_unique_character('leetcode')}")