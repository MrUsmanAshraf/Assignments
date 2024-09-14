# Steps to solve the assignments
1. The task was to create a python program that take 3 numbers as input.
2. i started this task by taking a variable named __*name*__ to take input of name of the user.
```python 
name: str= str(input("Enter your name: "))
```
3. Next step was to ask user to enter three of there favorite numbers. so i choose an empty list named __*numbers*__.
```python
numbers = []
```
4. after that a *for* loop was used to take input 3 times from user. and use these number in our empty list named **numbers**.
```python
for number in range (3):
    number=int(input(f"Enter your favorite number : "))
    numbers.append(number)
```
5. then a statement was printed with the name that user gave input at the start of program that lets explore your favorite numbers.
```python 
print(f"Hello, {name} Let's explore your favorite numbers.")
```
6. after that a conditional statement of if-else was used to find out if given numbers are eben or odd.
```python
for number in numbers:
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
```
7. Than a **for** statement was used to print the number and its square.
```python 
for number in numbers:
    print(f"the number {number} and its square is: {number, number **2}")
```
8. A new variable named **number_sum** was declared and sum of all numbers was stored in that new variable and it was printed as well.
```python
numbers_sum =(sum(numbers))
print(f"Amazing! the sum of your favorite numbers is:  {numbers_sum}.")
```
9. Next task was to check if sum of given numbers was a prime number or not? For this purpose a **function** named *prime_num* was defined.
```python
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
10. than finally conditional statement if-else was used to find if sum of numbers was a prime number or not.
```python
if prime_num(numbers_sum):
    print(f"{numbers_sum} is a prime number.")
else:
    print(f"{numbers_sum} is not a prime number.")
```
# complete code of given case was as below.
```python 
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
```

# Output of the code was as below.
```
Enter your name: usman
Enter your favorite number : 3
Enter your favorite number : 4
Enter your favorite number : 5
Hello, usman Let's explore your favorite numbers.
The number 3 is odd.
The number 4 is even.
The number 5 is odd.
the number 3 and its square is: (3, 9)
the number 4 and its square is: (4, 16)
the number 5 and its square is: (5, 25)
Amazing! the sum of your favorite numbers is:  12.
12 is not a prime number.
```