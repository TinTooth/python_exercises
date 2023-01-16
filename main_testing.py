from find_first_and_last_postion import Solution

test1 = Solution([5,7,7,8,8,10])
print(test1.searchRange(7))
print(test1.searchRange(8))
print(test1.searchRange(10))
print(test1.searchRange(5))
print('not on list')
print(test1.searchRange(2))
print(test1.searchRange(6))
print(test1.searchRange(12))
