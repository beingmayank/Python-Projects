# converting the given list into dictionary

l = ['gauravtomar186','555kumar','ravi55sharma']
l2=[]
l3=[]
for i in l:
    s = ""
    s2=""
    for j in i:
        if(j.isdigit()):
            s=s+j
        else:
            s2 = s2+j
    l2.append(s)
    l3.append(s2)
print(l2)
g= dict(zip(l2,l3))
print(g)
    