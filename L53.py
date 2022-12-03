#Kaylen Nyhuis and Emily Rusch
n = input("Enter a number \n")
def perfect_number(n):
    sum = 0
    for z in range(1, n):
        if n % z == 0:
            sum += z
    return sum == n

print(perfect_number(int(n)))
