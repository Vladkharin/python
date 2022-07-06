# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)

# # print(b)

# print(list(filter(lambda elem: elem < 5, a)))

from unittest import result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     c.append(i)
# for i in b:
#     c.append(i)

# c.sort()

# print(c)

# result = list(filter(lambda elem: elem in b, a))


# result = [elem for elem in a if elem in b]

# result = list(set(a) & set(b))
# print(result)

c = dict(a)

print(c)

