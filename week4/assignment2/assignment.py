nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums | letters)
nums.update(letters)
print(nums)

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}