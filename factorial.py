def factorial(n:int):
    if(n == 1 or n == 0):
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    fat7 = factorial(7)
    print(fat7)