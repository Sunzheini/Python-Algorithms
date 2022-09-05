# Searching and Sorting Algorithms

# -----------------------------------------------------------------------------------------------
# Linear Search - check elements one by one, i.e. for an element in a list

# nums = [1, 2, 3, 4, 5, 6, 7]
#
# target = 5
# for idx, i in enumerate(nums):
#     if i == target:
#         print(f"Index of target is {idx}")
#         break


# -----------------------------------------------------------------------------------------------
# Binary Search - spisykyt v koito tyrsim trqbva da e predvariteln o podreden
                # sled tova sravnqvame sys sredniq element
                # postoqnno svivame masiva na 2

# nums = [1, 2, 3, 4, 5, 6, 7]
# target = 5

# -----------------------------------------------------------------------------------------------

# 1
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))





