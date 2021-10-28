nums =[2,3,5,7,8,12]

# def mapFunction(num):2  #map
#     return num**2
# nums = list(map(mapFunction,nums));
# print(nums)

# nums=[num**2 for num in nums] #comprehension way
# print(nums)

# ___lambda___

nums = list(map(lambda num:num**2,nums))
print(nums)