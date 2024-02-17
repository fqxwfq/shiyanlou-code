def away7(i):
    if i%7<1 or i%10==7 or ((i//10)^10==7):
        return 0
    else:
        return 1

for i in range(1,101):
    if away7(i):
        print(i)

