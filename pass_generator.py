#You have Python3 install to use this script 
#Executing command 
#s=list[2,4,6].split
#$python3 pass_generator.py
string = input("Enter The Words You Want separated by commos :> ")
a = string.split(",")
n = (int(input("Enter number of Words you input above"))+1)
x = n
import itertools
for e in range(x):
    for i in itertools.permutations(a,e):
        print(''.join(i))
