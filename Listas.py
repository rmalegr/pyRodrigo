
#Listas de Comprension
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
fruits.sort(reverse=True)
print(fruits)
#sorted(): returns the ordered list without modifying the original list Example:
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]

num1.extend(num2)
print(num1)


positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]

integers = positive_numbers + zero + negative_numbers

print(integers)