#This a python program to solve the Josephus problem
n=input("Enter the number of people sitting in the circle ")
def Survivor(n):
    x=1
    while x <= int(n):
        x = x * 2

    return (2 * int(n)) - x + 1

print ("The survivor is in the place ", Survivor(int(n)))
