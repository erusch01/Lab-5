#Kaylen Nyhuis and Emily Rusch
#Part A
x = 2
if x < 3:
    print("Small")

x=5
if x < 3:
    print("Small")

score = 8 #A score on a 10 point quiz
if score > 6:
    print("Nice work!")

for i in range (1,16):
    if i % 2 == 0:
        print(i, "is even")
#Part B
x =2
if x<3:
    print("Small")
else:
    print("Large")

x = 5
if x<3:
    print("Small")
else:
    print("Large")

score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score<9:
    print("Nice work!")
else:
    print("Excellent!")

for i in range (-2,3):
    if i % 2 == 0:
        print (i, "is even")
    else:
        print(i, "is odd")
#Part C
print(3<4)
print(4>2)
type(True)

if True:
    print("This text will always appear")
if False:
    print("This text will not appear")

def variable(x):
    if x>10:
        return True
    else:
        return False

print(variable(4))
