import os
import time

def add-numbers(numbers):
  sum=0
  for num in numbers:
    sum += num
  return sum

def subtract-two-numbers(num1, num2):
  return abs(num1-num2)
  
numbers = [21,43,54,6,67]

print(add-numbers(numbers))

print(subtract-two-numbers(21,54))
