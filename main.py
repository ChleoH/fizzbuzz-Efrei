def is_fizz(n):
    return n % 3 == 0 or '3' in str(n)

def is_buzz(n):
    return n % 5 == 0 or '5' in str(n)

def fizzbuzz(nombre):
    print("Entrée | Sortie")
    print("----------------")
    i= nombre
    if i == nombre:
        result = ""
        if is_fizz(i):
            result += "Fizz"
        if is_buzz(i):
            result += "Buzz"
        
        print(f"{i:<6} | {result if result else i}")

fizzbuzz(25)