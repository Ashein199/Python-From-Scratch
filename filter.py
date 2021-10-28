nums = [1,2,3,4,5,6,7,8,9,10]

# def even(num): #filter way
#     return (num%2)==0
# even_nums = list(filter(even,nums))
# print(even_nums)

# ____ lambda____
even_nums =list(filter(lambda num:(num%2)==0,nums))
print(even_nums)


# nums = [num for num in nums if(num%2)==0] #comprehension way
# print(nums)

# even_nums = [] #normal way
# for num in nums: 
#     if(num%2)==0:
#         even_nums.append(num)
# print(even_nums)