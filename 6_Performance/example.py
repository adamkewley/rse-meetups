def f(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def slow_function():
    result1 = f(100000)
    result2 = ''
    for i in range(10000):
        result2 += str(i)
    result3 = sum([i for i in range(1000000)])
    result4 = 0
    for i in range(10000000):
        result4 += len(str(i))

if __name__ == "__main__":
    slow_function()
