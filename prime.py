def prime_num_calc(num):
    mod = 0
    cnt = 0
    if num == 1 or num == 2:
        prime = True
    else:
        num1 = num + 1
        for xyz in range(1,num1):
            mod = num % xyz
            if mod == 0:
                cnt = cnt + 1
            else:
                mod = 0
    if cnt == 2:
        prime = True
    else:
        prime = False
    return prime
number = int(input("Please enter which number you want to check is prime or not"))
print(prime_num_calc(number))





