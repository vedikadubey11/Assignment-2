import random 
import string

print("Welcome to password  generator")

lower = string.ascii_lowercase 
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower+upper+digits+symbols
length = int(input("enter the length of password:"))
password = random.sample(all,length)
password = "".join(password)

print("password is :",password)
