print("1. RRR\n2. KGF\n3. Pathan\n4. Tiger\n5. War")
y = int(input("Select which movie you want to show:- "))
if (y>=1 and y<=5):
    print("1.you pay: Rs.600/person for last seats\n2.you pay: Rs.300/person for middle seats\n3.you pay: Rs.200/person for first seats")
    x = int(input("Enter your choice:- "))
    if (x == 1):
        mem = int(input("Number of members: "))
        a = 600
        total = a*mem
    elif (x == 2):
        mem = int(input("Number of members: "))
        b = 300
        total = b*mem
    elif (x == 3):
        mem = int(input("Number of members: "))
        c = 200
        total = c*mem
    else:
        print("Enter a correct option.")
    print("Your total amount is Rs.", total)
else:
    print("Please select a correct choice.")
