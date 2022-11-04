def process_item(x: int):
    is_prime = [1]*(x*2)
    is_prime[0] = 0
    is_prime[1] = 0
    i = 2
    while i * i <= x*2:
        if is_prime[i] == 0:
            i += 1
            continue
        j = 2*i
        while j < x*2:
            is_prime[j] = 0
            j += i
        i += 1

    for i in range(x+1, x*2):
        if is_prime[i] == 1:
            return i


if __name__ == '__main__':
    user_input = int(input("Enter a natural number: "))
    print("The least prime number greater than x is: " + str(process_item(user_input)))