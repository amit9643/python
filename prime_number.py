num =int(input())
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("false")
            break
    else:
        print("true")

else:
    print("false")
