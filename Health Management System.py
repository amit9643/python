def gettime():
    import datetime
    return datetime.datetime.now()


def take(a):
    if(a==1):
        b= int(input("Enter 1 for Excerise and 2 for food\n"))
        if(b==1):
            value = input("Type here,\n")
            with open("HarryExcr.text","a") as f:
                f.write(str([str(gettime())]) +":" + value+"\n")
                print("Sucessfully")
        elif b==2:
            value = input("Type here,\n")
            with open("HarryFood.text", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
                print("Sucessfully")
    elif a==2:
        b = int(input("Enter 1 for Excerise and 2 for food\n"))
        if (b == 1):
            value = input("Type here,\n")
            with open("RohanExcr.text", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
                print("Sucessfully")
        elif b == 2:
            value = input("Type here,\n")
            with open("RohanFood.text", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
                print("Sucessfully")
    elif a==3:
        b = int(input("Enter 1 for Excerise and 2 for food\n"))
        if (b == 1):
            value = input("Type here,\n")
            with open("HammadExcr.text", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
                print("Sucessfully")
        elif b == 2:
            value = input("Type here,\n")
            with open("HammadFood.text", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
                print("Sucessfully")
    else :
        print("Invalid Input")

def retrieve(a):
            if a==1:
                c=int(input("Enter 1 for Excerise 2 For Food\n"))
                if c==1:
                    with open("HarryExcr.text") as f:
                        for i in f:
                            print(i,end="")
                elif c==2:
                    with open("HarryFood.text") as f:
                        for i in f:
                            print(i, end="")
            elif a==2:
                c=int(input("Enter 1 for Excerise 2 For Food\n"))
                if c==1:
                    with open("RohanExcr.text") as f:
                        for i in f:
                            print(i,end="")
                elif c==2:
                    with open("RohanFood.text") as f:
                        for i in f:
                            print(i, end="")
                else:
                    print("Invalid key")

            elif a == 3:
                c = int(input("Enter 1 for Excerise 2 For Food\n"))
                if c == 1:
                    with open("HammadExcr.text") as f:
                        for i in f:
                            print(i, end="")
                elif c == 2:
                    with open("HammadFood.text") as f:
                        for i in f:
                            print(i, end="")
                else:
                    print("Invalid key")
            else:
                print("Invalid Number")
print("Health Management System")
N = int(input("press 1 for log and 2 for retrieve\n"))

if N == 1:
    a= int(input("press 1 for harry 2 for Rohan 3 for hammad \n"))
    take(a)
else :
    a = int(input("press 1 for harry 2 for Rohan 3 for hammad"))
    retrieve(a)
