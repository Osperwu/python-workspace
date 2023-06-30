# nums = set([1, 2, 3, 4, 3, 2, 1, 5])

# print(type(nums))
# print(nums)
# nums1 = {1, 2, 3}
# nums2 = {3, 4, 5}
# nums = nums1.union(nums2)
# # nums = nums1 + nums2
# print(nums)

nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odds = {1, 3, 5, 7, 9}
even = nums ^ odds
print(even)  # {0, 2, 4, 6, 8, 10}
print(even | odds)
print(nums & even)
print(nums ^ even)
