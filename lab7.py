# CS3
# Angel Rodriguez II
# Lab 6
# Diego Aguirre
# 12-08-2019
# Purpose: The purpose of this lab is to solve the edit distance problem.

def edit_distance(str1, str2, m , n):
    if m==0: 
         return n

    if n==0: 
        return m 
    
    if str1[m-1]==str2[n-1]: 
        return edit_distance(str1,str2,m-1,n-1)
    
    return 1 + min(edit_distance(str1, str2, m, n-1), edit_distance(str1, str2, m-1, n), edit_distance(str1, str2, m-1, n-1))
