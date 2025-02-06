def is_fizz(n):
    return n % 3 == 0 or '3' in str(n)

def is_buzz(n):
    return n % 5 == 0 or '5' in str(n)

def fizzbuzz():
    for i in range(1, 101):
        result = ""
        if is_fizz(i):
            result += "Fizz"
        if is_buzz(i):
            result += "Buzz"
        
        print(result if result else i)

fizzbuzz()