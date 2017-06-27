# def secret(s):
#     i = 0
#     result = ''

#     while not s[i].isdigit():
#         result = result + s[i]
#         i = i + 1
   
#     return result
# print (secret('123'))
# #print (secret('abc'))
# print (secret('abc123'))
# print (secret('123abc'))

# def example(L):
#     """ (list) -> list
#     """
#     i = 0
#     result = []
#     while i < len(L):
#         result.append(L[i])
#         i = i + 3
#     return result

# print (example([1,2,3,4,5,6,7,8,9,10]))

# sum = 0
# i = 524
# while i<=10509:
# 	sum += i
# 	i += 2

# print (sum)

# sum = 0
# for i in range(524, 10509, 2):
# 	sum += i

# print (sum)

# sum = 0
# i = 1523
# while i<=10504:
#   sum += i
#   i += 2

# print (sum)

# sum = 0
# for i in range(1523, 10504, 2):
#   sum += i

# print (sum)


# def increment_items(L, increment):
#     i = 0
#     while i < len(L):
#         L[i] = L[i] + increment
#         i = i + 1

# values = [1, 2, 3]
# print(increment_items(values, 2))
# print(values)


values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)

values = []
for num in range(1, 3):
    values.append(num * 3)
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)

values = []
for num in range(3, 9, 3):
    values.append(num)
print(values)

# for num in range(3,20,8):
#     print(num)