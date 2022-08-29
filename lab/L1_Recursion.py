# Recursion


# metod za reshavane na problemi, koito predstavlqva edna funkciq, koqto se samoizvikva


# 1
# def array_sum(array, start):
#     if start == len(array) - 1:           # dyno: len(array) - 1 e posledniq index
#         return array[start]               # bazov case: kogato imame 1 element
#     return array[start] + array_sum(array, start+1)
#
# # array_sum(array, start+1 e rekursivno izvikvane
# # start + 1 e stypka
#
#
# numbers = [int(x) for x in input().split()]
# print(array_sum(numbers, 0))


# 2
# def factorial(start):
#     if start == 0:
#         return 1
#     return start * factorial(start-1)
#
#
# number = int(input())
# print(factorial(number))


# 3
# def drawing(n):
#     if n == 0:
#         return
#
#     print('*' * n)      # pre-action
#     drawing(n-1)        # recursive call
#     print('#' * n)      # !!!post-action!!! izpylnqva se na vryshtane sled prikliuchvane na rekursiqta
#
#
# number = int(input())
# drawing(number)
# #
# # ****
# # ***
# # **
# # *
# # #
# # ##
# # ###
# # ####


# 4
# not done


# ------------------------------------------------------------------------------
# Backtracking










