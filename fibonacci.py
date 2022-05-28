def fibonacci(n:int):
    if(n < 1):
        return 0
    elif(n <= 2):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range(100):
        print(fibonacci(i))