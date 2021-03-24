import random


print("Welcome To Your Password Generator")

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ !@#$%^&*().,?0123456789'
number =input("Enter Amount of password to generate: ")

number=int(number)

length=input("Your password key length: ")
length=int(length)
print('\n here Your passwords:  ')

for pwd in range(number):
  passwords=''
  for c in range(length):
    passwords+=random.choice(chars)
  print(passwords)