def fizzbuzz(num):
    if num%3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num%3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

def main():
    for i in range(1, 101):
        if i%3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(str(i))

if __name__ == '__main__':
    main()