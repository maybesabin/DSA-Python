stock_prices = [300, 301, 305, 307, 400]

#On what day price was 305?
def find_day():
    for x in range(len(stock_prices)):
        if stock_prices[x] == 305:
            return x # O(n) complexity
        

#Adding value on index 0
def add_value():
    stock_prices.insert(0, 205)
    return stock_prices

#Deleting value on index 1
def del_value():

    stock_prices.pop(1)
    return stock_prices


#2 dimensional arrays

random_numbers = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

# print(random_numbers[1][1]) prints 5



#Excercise1

monthlyExpenses = [
    {"January":2200},
    {"February":2350},
    {"March":2600},
    {"April":2130},
    {"May":2190},
]


#1. In Feb, how many dollars you spent extra compare to January?

def extraSpent():
    expense = monthlyExpenses[1]["February"] - monthlyExpenses[0]["January"]
    return expense



#2. Find out your total expense in first quarter (first three months) of the year.
def totalExpense():
    total = monthlyExpenses[0]["January"] + monthlyExpenses[1]["February"] + monthlyExpenses[2]["March"]
    return total


#3. Find out if you spent exactly 2000 dollars in any month
def checkExpense():
    for i in range(len(monthlyExpenses)):
        if list(monthlyExpenses[i].values())[0] == 2000:
            return i


#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def addExpense():
    monthlyExpenses.append({"June":3500})
    return monthlyExpenses


#5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

def editExpense():
    monthlyExpenses[3]["April"] -= 200
    return monthlyExpenses



#Excercise 2

heros=['spider man','thor','hulk','iron man','captain america']

#1. Length of the list
print(len(heros))

#2. Add 'black panther' at the end of this list
heros.append("black panther")

#3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, "black panther")


# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros [1:3] = ["doctor strange"]


# 5. Sort the heros list in an alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()



#Excercise 3
#Create a list of all odd numbers between 1 and a max number. Max number is something you 
# need to take from a user using input() function

def oddNumbers(maxNum):
    myList = []
    for i in range(1,maxNum,2):
        myList.append(i)
        
    return myList

print(oddNumbers(10))
        