#1 Count no of even and odd in an  array 

def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    for x in range(len(arr)):
        if arr[x] % 2 == 0:
            even_count += 1;
        else:
            odd_count +=1;

    return even_count, odd_count

arr = [1,2,3,4,5,6]

even_count, odd_count = count_even_odd(arr)
print(f"Even: {even_count} & Odd: {odd_count}")


#2 Average of an array

def average(arr):
    return sum(arr) / len(arr)

arr = [1,2,3,4,5,6]

print(average(arr))



#3 Check if a number is palindrome

def check_palindrome(num):
    temp = num
    reversed_num = 0
    while num!=0:
        digit = num%10;
        reversed_num = reversed_num*10 + digit;
        num = num//10
    
    if(temp == reversed_num):
        return "Palindrome"
    
    else:
        return "Not Palindrome"

print(check_palindrome(121))
print(check_palindrome(500))


#4 Count vowels in a string

def count_vowels(s):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for x in range (len(s)):
        if s[x].lower() in vowels:
            count += 1

    return count


print(count_vowels("SABIN"))

 

#5 Finding Largest element in an array

def largest_element(num):
    largest = num[0]

    for x in range(len(num)):
        for y in range (x+1, len(num)):
            if num[y] > largest :
                largest = num[y]
    return largest

num = [1,2,3,4,5,6,17]
print(largest_element(num))


# 6 Two Sum

def two_sum(arr, target):
    result = []
    for i in range(0, len(arr)):
        for j in range (i+1, len(arr)):
            if(arr[i] + arr[j] == target):
                result.append([arr[i],arr[j]])
    return result
arr = [1,2,3,4,5,6,7,8]
target = 9
print(two_sum(arr,target))


#7 Best & worst time to buy stock

def stock_buy(stock_arr):

    if(len(stock_arr)<2):
        return "Not Enough Data"

    min_price = stock_arr[0]
    max_price = stock_arr[0]

    for x in range(len(stock_arr)):
        if stock_arr[x] < min_price:
            min_price = stock_arr[x]
        
        elif stock_arr[x] > max_price:
            max_price = stock_arr[x]

    return min_price, max_price

stock_arr = [2]
print("The best & worst day to buy stocks is: ",stock_buy(stock_arr))


#8 Returns true or false if duplicates in an array

def find_duplicate(arr):

    for i in range(len(arr)):
        for j in range (i+1, len(arr)):
            if(arr[i] == arr[j]):
                return True
            else:
                return False

arr = [1, 0, 2, 3, 4]
print(find_duplicate(arr))


#9 Product except self

def ProductExceptSelf(num):
    length = len(num)
    
    left = [0] * length
    right = [0] * length
    result = [0] * length

    # Initialize the first element of left product array to 1
    left[0] = 1
    for i in range(1, length):
        left[i] = left[i-1] * num[i-1]
    
    # Initialize the last element of right product array to 1
    right[length - 1] = 1
    for i in range(length-2, -1, -1):
        right[i] = right[i+1] * num[i+1]

    # Construct the result array
    for i in range(length):
        result[i] = left[i] * right[i]

    return result

num = [1, 2, 3, 4, 5]
print(ProductExceptSelf(num))
