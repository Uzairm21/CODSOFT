import random

Lower='abcdefghijklmnopqrstuvwxyz'
Upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Number='0123456789'

length=int(input("Enter the length of password : "))

def Pass_Gen(length):
  all=Lower+Upper+Number
  return ''.join(random.choice(all) for _ in range(length))

password = Pass_Gen(length)  
print("Generated Password:", password)
