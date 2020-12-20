import random
print("WELCOME TO  PASSWORD GENERATOR")
print("HERE ,YOU WILL BE ASKED TO ENTER THE FIRST FOUR CHARACTERS AND THEN YOU WILL BE GIVEN A RANDOM STRONG PASSWORD")
t=input("ENTER ANY FOUR DIGITS-CHARACTERS OF YOUR CHOICE WHICH YOU WOULD LIKE TO INLCUDE IN YOUR PASSWORD\n")
def special():
   s="~!@#$%^&*_+?><:\-*./"
   t=s[random.randint(0,19)]
   return t
def character():
   s="QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklmnbvcxz"
   t = s[random.randint(0,51)]
   return t
def digit():
   s="7410852963"
   t = s[random.randint(0,9)]
   return t
def para():
   s="dfgsdgfdfgsfffgFBuggfYYtyvAQWAESDXFyuhfxdyhuvjcnYUFDHNVyhufjfhuyjvDHYFDBHNJDChbdfbfhfhBEUBFDqdsyfhjhjkgWUHDSGHr"
   t = s[random.randint(0, 110)]
   return t
t=t[::-1]
pas=character()+t[3]+digit()+t[1]+special()+t[0]+para()+t[2]
print("YOUR PASSWORD IS "+pas)

