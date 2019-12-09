# CS3
# Angel Rodriguez II
# Lab 6
# Diego Aguirre
# 12-08-2019
# Purpose: The purpose of this code is to test the edit distance problem.

from lab7 import edit_distance

str1 = "failure"
str2 = "success"
min_change = edit_distance(str1, str2, len(str1), len(str2))

print("-----------------------------")
print("Original word: " + str1)
print("Other word: " + str2)
print("Minimum # of changes: " + str(min_change))
print("-----------------------------")

str1 = "Elephant"
str2 = "Elephants"
min_change = edit_distance(str1, str2, len(str1), len(str2))

print("Original word: " + str1)
print("Other word: " + str2)
print("Minimum # of changes: " + str(min_change))
print("-----------------------------")

str1 = ""
str2 = "Angel"
min_change = edit_distance(str1, str2, len(str1), len(str2))

print("Original word: " + str1)
print("Other word: " + str2)
print("Minimum # of changes: " + str(min_change))
print("-----------------------------")

str1 = "Rodriguez"
str2 = ""
min_change = edit_distance(str1, str2, len(str1), len(str2))

print("Original word: " + str1)
print("Other word: " + str2)
print("Minimum # of changes: " + str(min_change))
print("-----------------------------")
