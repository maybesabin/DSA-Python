# #3 Sum

# def threeSum(nums, target):
#     length = len(nums)
#     result = []
#     for i in range(length):
#         for j in range(i+1,length):
#             for k in range(j+1,length):
#                 if (nums[i]+nums[j]+nums[k] == target):
#                     result.append((nums[i],nums[j],nums[k]))
    
#     return result

# nums = [-1,0,1,2,-1,-4]
# target = 9

# print(threeSum(nums, target))


# Valid Parenthesis

def validParenthesis (s):
    left_stack = ["(", "{", "["]
    right_stack  = [")", "}", "]"]

    if (s in left_stack & s in right_stack):    
        return True
    else:
        return False


s = "{}"
print(validParenthesis(s))