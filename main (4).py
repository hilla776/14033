max=0;
next=0;

for counter in range(4):
    next=int(input("give me the number"))
    if next>max:
        max=next
    
print(max)