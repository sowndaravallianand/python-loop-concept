# task 7
# fish and bus quize

num = int(input("Enter the Number :"))

for i in range(1,10):
    if i%3 !=0 and i%5!=0:
        print("Print fish")
    elif i%3 ==0:
        print("print bus")
    