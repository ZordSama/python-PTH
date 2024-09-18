# is odd or even
def is_odd(num):
    return num % 2 != 0
while True:
    num = int(input("Enter a number: "))
    if num >=0:
        if is_odd(num):
            print(f"{num} is odd")
        else:
            print(f"{num} is even")
        break
    print("Please enter a positive number")
    
    