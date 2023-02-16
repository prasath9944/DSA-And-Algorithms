# -*- coding: utf-8 -*-
"""Selection_Sort_Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_93njsy8-SjFdb2QVkwaTTk25rQWlMX4
"""

## Time Complexity : O(n^2)
## Function Definition
def selectionSort(arr):
  n=len(arr)
  for i in range(n):
    # to store the index of the minimum element
    min_index=i
    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
    # swap of the element at i and min_index
    arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr
# Driver Code
arr=[50,38,75,29,11,17,20,37]
# Function Calling
result=selectionSort(arr)
print("Selection Sort of the given array elements is :",result)
