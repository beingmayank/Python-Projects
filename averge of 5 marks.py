print("Enter five subject marks:-")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
sum = (a+b+c+d+e)
per = (sum/500)*100
print("Your percentage is",per,"%")
if(70<per and per<=100):
    print("You are select for inteview")
    interview = int(input("Enter your interview marks:- "))
    if(70<interview and interview<=100):
        print("You are selected for company.")
else:
    print("You are not eligible for interview.")
print("Thank You!")