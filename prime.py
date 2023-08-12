def prime_num_calc(num):#accepts 1 arg
    #Add varible, you'll see why i use it shortly
    cnt = 0
    if num == 1 or num == 2:#Methodology wont work for 1 and well, why not 2 then
        prime = True
    else:#if the number is not 1 or 2 we'll let the computer compute it for us
        num1 = num + 1#because of a quirk in range() where it only goes up to the_last_number-1
        for xyz in range(1,num1):#uses that quirky range function, really convienent for beginners tho
            mod = num % xyz#here is where we use that modulo operration, if you dont know what it does basically just tell you the remainder of a division, in this case the division of the number you're check with whatever number between it and 1, I think you see where i am going
            if mod == 0:#if num is divisible by xyz
                cnt = cnt + 1#cnt records the number of numbers num is divisble by
            else:
                mod = 0#resets mod, not neccessary but since python is dynamic i do anyways
    if cnt == 2:#if it is divisible by 2 numbers, namely itself and 1, it is a prime number, so we set the boolean prime to True
        prime = True
    else:#im getting tired of writing this, but this if that previous statement is false, sets prime to False,
        prime = False
    return prime#returns the boolean prime's value to where is it called
number = int(input("Please enter which number you want to check is prime or not"))#takes the input of what number you check, and makes it a intenger
print(prime_num_calc(number))#prints the value of boolean prime in the function i defined earlier, number gets passed as num





