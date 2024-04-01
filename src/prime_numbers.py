def is_prime(num):
    square = round(num ** 0.5); i = 2
    prime_ = True

    while prime_ and i <= square:
        prime_ = True if num%i != 0 else False
        i += 1
    
    return prime_

for i in range(1, 20):
    if is_prime(i+1):
        print(i+1, end=" ")