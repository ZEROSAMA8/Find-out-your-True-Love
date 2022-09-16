# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
com_name=name1+name2
loname= com_name.lower()
t = loname.count("t")
r = loname.count("r")
u = loname.count("u")
e = loname.count("e")
true = t + r + u + e
l = loname.count("l")
o = loname.count("o")
v = loname.count("v")
e = loname.count("e")
love = l + o + v + e
total= str(true) + str(love)
totalint= int(total)
if totalint <10 or totalint>90:
    print(f"Your score is {totalint}, you go together like coke and mentos.")
elif totalint >=40 and totalint <= 50:
    print(f"Your score is {totalint}, you are alright together.")
else:
    print(f"Your score is {totalint}.")




