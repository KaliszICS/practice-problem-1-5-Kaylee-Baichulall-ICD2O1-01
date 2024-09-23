'''
Lesson 1.5 - Type casting(converting) and documentation
Author: Kaylee Baichulall
Date Created: Sept 23, 2024
Date Last Modified: Sept 23, 2024
'''
def q1():
  int1 = input("Input an integer: ")
  int1 = int(int1)
  print(int1 + 3)

def q2():
  num1 = input("Input a number: ")
  num1 = str(num1)
  num1 = (num1 + "4")
  num1 = float(num1)
  print(num1)

def q3():
  radius = input("Input a radius: ")
  radius = float(radius)
  radius = radius * radius * 3.14

def q4():
  num2 = input("Input a number: ")
  num2 = float(num2)
  num2 = num2 * 12
  num2 = int(num2)
  print(num2)

def q5():
  num3 = input("input a integer: ")
  num3 = int(num3)
  num3 = num3 + 5
  print(f"Your number + 5 is {num3}")


#Comment this code out when running tests
#Do not comment this out when running your program normally

q1()
q2()
q3()
q4()
q5()
