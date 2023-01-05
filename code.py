import sys
def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

print("Enter a number:")
while True: #in the case that there is an invalid input, loop until valid integer is given.
    
    try:
        num = int(input())
        while num != 1:
            num = collatz(num)
        break #break once 1 is returned.
    except ValueError:
        print("Please enter a valid integer.")
        continue

sys.exit() #end program.
