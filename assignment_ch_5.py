name: str= str(input("Enter your name: "))
numbers = []
for number in range (3):
    number=int(input(f"Enter your favorite number : "))
    numbers.append(number)
print(f"Hello, {name} Let's explore your favorite numbers.")
for number in numbers:
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
for number in numbers:
    print(f"the number {number} and its square is: {number, number **2}")
numbers_sum =(sum(numbers))
print(f"Amazing! the sum of your favorite numbers is:  {numbers_sum}.")
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
if prime_num(numbers_sum):
    print(f"{numbers_sum} is a prime number.")
else:
    print(f"{numbers_sum} is not a prime number.")

