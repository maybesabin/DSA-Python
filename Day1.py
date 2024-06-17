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