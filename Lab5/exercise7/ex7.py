"""
Write a function called process that receives a variable number of keyword arguments
The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
- If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
- If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
- If the function receives a parameter called offset, it will skip that number of entries from the beginning of the
result list.

The function will return the processed numbers.
"""


def fibo(n: int):
    elements = [0, 1]
    for i in range(2, n + 1):
        elements.append(elements[-1] + elements[-2])
    return elements


def process(**kwargs):
    fibo_elements = fibo(1000)
    if "filters" in kwargs.keys():
        fibo_elements = [number for number in fibo_elements if all([p(number) for p in kwargs["filters"]])]
    if "offset" in kwargs.keys():
        fibo_elements = fibo_elements[kwargs["offset"]:]
    if "limit" in kwargs.keys():
        fibo_elements = fibo_elements[:kwargs["limit"]]
    return fibo_elements


def sum_digits(x):
    return sum(map(int, str(x)))


if __name__ == '__main__':
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                  limit=2,
                  offset=2
                  ))
