lower=int(input("enter the starting number"))
upper=int(input("enter the ending number"))
for num in range (lower,upper+1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            print(num)
